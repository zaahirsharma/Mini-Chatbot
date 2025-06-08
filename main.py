# Created by Zaahir Sharma
# langchain is a framework that allows to build AI applications
# langgraph is complex framework that allows to build AI agents
# dotenv module allows to load environment variable files within python script (.env file)
# Difference between AI applications and AI agents is that agent has access to tools
# Allows program to actually do something rather than just respond to message

from langchain_core.messages import HumanMessage
# Used to connect to OpenAI and have LLM running
from langchain_openai import ChatOpenAI
# Used to register tool that AI agent can use
from langchain.tools import tool
# 
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

import sys

# Looks in current directory for .env file and loads in variables for later use
load_dotenv()

# Tool decorator to create tool the agent can use
@tool
# Take in 2 floats and return a string
def calculator(a: float, b: float) -> str:
    # Describing the tool for agent time of use
    """Useful for performing basic addition arithmetic with numbers"""
    print("Calculator Tool has been called")
    return f"The sum of {a} and {b} is {a + b}"

@tool
def say_goodbye() -> str:
    """Useful for when user says goodbye or wishes to end the conversation"""
    print("Goodbye tool has been called. Type 'quit' to end conversation.")
    return "I hope I could be of assitance!"

# Initialize chatbot and AI agent
def main():
    model = ChatOpenAI(temperature=0) # Higher temperatrue increases randomness in model, temperature=0 means no randomness
    
    # To be filled with tools to be used by agent
    tools = [calculator, say_goodbye] 
    # Create agent, plugging in model and tools for it to use
    agent_executor = create_react_agent(model, tools)


    print("Welcome! I'm you personal AI assitant. Type 'quit' to exit.")
    print("Feel free to chat with me or ask for math assitance.")
    
    # Keep looping so user can keep interacting with model
    while True:
        # Removes any white space from beginning or end of input
        user_input = input("\nYou: ").strip()
        
        # Exit loop, end program if user types exactly the word'quit'
        if user_input.lower() == 'quit':
            print("Manual Exit. Goodbye!")
            break
        
        # AI response, end with nothing (no ending \n character)
        # Response will follow the Assitant: statement as a result, not on new line
        print("\nAssistant: ", end="")
        # Stream response from LLM using agent_executor
        # Pass in messages to stream to agent using dictionary
        # One message to respond to which is a HumanMessage which is held in variable user_input
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            # Check if chunk response is from agent
            # Check if any messages are in the response
            # If so, loop through them
            if "agent" in chunk and "messages" in chunk["agent"]:
                # Grab all message and print out all message content
                # End with empty string, end with empty line
                # Stream longer responses from agent, so it looks word by word
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
                
        print()
        
# Execute main function if this python file is called directly
if __name__ == "__main__":
    main()
                
        
    
    


