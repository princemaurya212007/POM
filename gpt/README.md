## Chatbot

### Getting started

1. Please update `.env` file with the `OPENAI_API_KEY`. The content of `.env` file will be as follows:

```
OPENAI_API_KEY=<open-ai-api-key>
```

Replace `<open-ai-api-key>` with OpenAI API key.

2. Install the packages needed by running the following command

```
pip install -r requirements.txt
```

3. Run `main.py` file to start the chat session.

4. Press `exit` to exit the session.

### Model

`gpt-3.5-turbo` is being used to build the chatbot. It is designed to be used for various natural language processing tasks such as text generation, language translation and answering questions.

**API kEY**: It is used for authentication while making the request to OpenAI API. It is crucial for maintaining authorized access to the OpenAI API and also for tracking billing information

**openailChatCompletion.create**: This method is used to interact with the GPT model. It sends a request to to the OpenAI API and process the conversation held so far and generate a response based upon the context of the chat.
