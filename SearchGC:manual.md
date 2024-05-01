# NLM Powered Search Processor for Guitar Center

The NLM Powered Search Processor is a web-based application that leverages OpenAI's GPT and Whisper models to provide an enhanced search experience. This document serves as a comprehensive guide to setting up, deploying, and using the application.

## Quick Install

Before you begin, ensure you have Python 3.8 or higher installed on your system. You will also need Docker for containerization.

## Installation

1. Clone the repository containing the source code to your local machine.
2. Navigate to the project directory and install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Setting Up the Environment

To securely manage the OpenAI API key, you will need to generate a Fernet key:

```bash
from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key.decode())
```

Set the generated key as an environment variable `FERNET_KEY`.

## Running the Application Locally

1. Start the Flask application:

```bash
python main.py
```

2. Open your web browser and navigate to `https://localhost:5000` to access the application.

## Using the Application

### Text Search

1. Enter your search query in the provided text field.
2. Click the 'Search' button to process your query using GPT.
3. The search results will be displayed on the webpage.

### Voice Search

1. Click the 'Voice Search' button and speak your query.
2. The application will transcribe your voice input using Whisper and display the transcription.
3. The search results based on your voice query will be displayed on the webpage.

### API Key Input

1. Upon first use, the application will prompt you to enter your OpenAI API key.
2. Enter your key and submit it. The application will validate and store the key securely for subsequent API requests.

## Containerization with Docker

1. Build the Docker image using the provided Dockerfile:

```bash
docker build -t nlm-search-processor .
```

2. Run the Docker container:

```bash
docker run -p 80:80 nlm-search-processor
```

3. Access the application through `http://localhost` on your web browser.

## Deployment

To deploy the application on a server, you can use the Docker container you've built. Ensure that the server has Docker installed and simply transfer the image or use the Dockerfile to build it on the server.

## Documentation and Testing

Comprehensive documentation is provided in the form of code comments and this manual. To test the application, follow the testing instructions outlined in the `testing.md` file (not provided here, but should be part of your project documentation).

## Final Deliverables

- A fully functional web-based demonstration of the NLM powered search processor ready for live testing.
- A deployment package including all source code, Dockerfiles for containerization, and deployment instructions.
- Comprehensive documentation outlining the system's features, development journey, and guidance for setup and testing.

For any further assistance or troubleshooting, please refer to the `troubleshooting.md` file (not provided here, but should be part of your project documentation) or contact our support team.