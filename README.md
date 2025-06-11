# Python AI Assistant with LangChain & LangGraph
## A Brief Introduction
This project demonstrates a Python-based conversational AI agent that leverages the power of Large Language Models (LLMs) through LangChain and LangGraph. Unlike a simple chatbot, this agent is equipped with custom tools, allowing it to perform specific actions—such as calculations—in response to user queries. This showcases the fundamental concepts of building intelligent agents with tool-use capabilities.

## Features
* Interactive Chat Interface: Engage with the AI assistant through a command-line interface.

* Tool-Augmented Responses: The AI agent can decide to use predefined tools to answer questions or perform tasks (e.g., a basic calculator for arithmetic).

* Conversational Flow Management: Designed to understand and respond appropriately, including recognizing when a user wishes to end the conversation.

* OpenAI Integration: Utilizes OpenAI's powerful language models for generating human-like responses.

* LangChain & LangGraph Core: Built on robust frameworks for developing sophisticated AI applications and agents.

## Tech Stack
This project is built primarily with Python and leverages modern AI frameworks:

* Python: The core programming language (requires Python 3.11 or higher).

* LangChain: A framework for developing applications powered by language models. It provides the building blocks for creating AI applications.

* LangGraph: An extension of LangChain, designed for building stateful, multi-step agentic behavior. It allows agents to perform sequences of actions.

* OpenAI: Provides the underlying Large Language Models (ChatOpenAI) for natural language understanding and generation.

* python-dotenv: Used for loading environment variables from a .env file, ensuring secure handling of API keys.

* uv: A modern and extremely fast Python package installer and resolver, used for dependency management.

### APIs Used
OpenAI API: This project interacts with the OpenAI platform, specifically using the ChatOpenAI model, to power the conversational capabilities of the AI assistant.

## Installation & Setup
To get a local copy of this project up and running, follow these simple steps:

Prerequisites:

* Ensure you have Python 3.11 or higher installed on your system.

* Install uv (if you don't have it already). You can install it via pip:

pip install uv

Or refer to the uv documentation for other installation methods.

### Clone the repository:

git clone https://github.com/[YourUsername]/[YourRepositoryName].git
cd [YourRepositoryName]

(Replace [YourUsername] and [YourRepositoryName] with your actual GitHub username and repository name).

### Install dependencies:
This project uses uv for dependency management.

uv pip install -e .

## Environment Variables Setup:
Create a file named .env in the root directory of your project. This file will store your OpenAI API key securely.

OPENAI_API_KEY=YOUR_OPENAI_API_KEY_HERE

OPENAI_API_KEY: Obtain your API key from the OpenAI Platform.

## Usage
Once installed and configured, you can run the AI assistant from your terminal:

python main.py

The assistant will greet you, and you can start interacting with it:

Welcome! I'm you personal AI assitant. Type 'quit' to exit.
Feel free to chat with me or ask for math assitance.

You: What is 5 + 3?
Assistant: The sum of 5.0 and 3.0 is 8.0

You: Hello there!
Assistant: Hello! How can I help you today?

You: I'm done. Goodbye.
Assistant: I hope I could be of assitance!

You: quit
Manual Exit. Goodbye!

Perform Calculations: Ask the assistant basic addition questions, and it will utilize its calculator tool.

End Conversation: Type quit (case-insensitive) to gracefully exit the assistant.

## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

License
This project is open-source.

Contact
Zaahir Sharma - sharma.zaahir@gmail.com - https://www.linkedin.com/in/zaahir-sharma/

Project Link: [[https://github.com/zaahirsharma/Mini-AI-Chatbot](https://github.com/zaahirsharma/Mini-AI-Chatbot)]
