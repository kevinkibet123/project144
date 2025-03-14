# Hugging Face API Trial Journey

This project documents my trial-and-error journey of integrating the Hugging Face Inference API. Instead of deleting previous versions, I decided to comment them out in "TRIAL NUMBER" sections to show my learning process.

## Features

Implements multiple API calls to Hugging Face models

Uses OpenAI-style chat completion and text extraction

Demonstrates iterative improvements in API integration

## Requirements

Ensure you have the following installed:

- Python 3.x

- requests

- huggingface_hub

### Install dependencies using:

'''python
pip install requests huggingface_hub

## Setup

Obtain an API key from Hugging Face.

Replace your_secret_api_key in the script with your actual API key.

Input your promt in *messages*

Run the script:

''python
python hfapi_model_deploy.api

## Trials Overview

- **Trial One**: Initial attempt using InferenceClient with deepseek-ai/DeepSeek-R1.

- **Trial Two**: Switched to using requests for API calls.

- **Final Version**: Integrated text extraction and a refined chat completion request.

### Output

The final version extracts text and sends it to the Hugging Face model for processing. The results are printed in both raw and cleaned formats.

## License

This project is open-source and available under the **MIT License**.