'''
TRIAL ONE
from huggingface_hub import InferenceClient

client = InferenceClient(
	provider="hf-inference",
	api_key="<your_secret_api_key>"
)

messages = [
	{
		"role": "user",
		"content": "Hi there. Please identify yourself"
	}
]

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1",
	messages=messages,
	max_tokens=1000
)
'''


'''
print(completion.choices[0].message)

<TRIAL TWO>

import requests

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer <your_secret_api_token>"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

data = query({"inputs": "Once upon a time"})
print(data)

'''

'''

import requests

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers = {"Authorization": "Bearer <your_secret_api_key>"}
payload = {
    "inputs": "Hello. Please identify yourself",
}

response = requests.post(API_URL, headers=headers, json=payload)
(response.json())
'''

from huggingface_hub import InferenceClient

client = InferenceClient(
	provider="hf-inference",
	api_key="your_secret_api_key"
)

messages = [
	{
		"role": "user",
		"content": "<Your prompt here>"
	}
]

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B", #To be honest, Deepseek isn't that good compared to Llama, o1, 4o etc. Plus the <thinking> doesn't look pretty in final output. Or maybe because this is a distilled model. You're taste.
	messages=messages,
	max_tokens=500 # Adjust according to the number of token your message requires.
)
final_result = completion.choices[0].message
print(final_result)
clean_result = completion.choices[0].message.content
print(clean_result)

