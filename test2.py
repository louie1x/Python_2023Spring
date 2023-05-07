# import wolframalpha

# # Set your App ID here
# app_id = "7K9HLL-WXEYKHQ3P7"

# # Create a client object with your App ID
# client = wolframalpha.Client(app_id)

# # Use the client object to query Wolfram Alpha
# res = client.query("What is the capital of France?")
# answer = next(res.results).text
# print(answer)

import wolframalpha

# Set your App ID here
app_id = "7K9HLL-WXEYKHQ3P7"

# Create a client object with your App ID
client = wolframalpha.Client(app_id)

# Use the client object to query Wolfram Alpha with a math question
res = client.query("What is 20*20?")
answer = next(res.results).text
print(answer)

# import openai

# # Set your OpenAI API key here
# openai.api_key = "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"

# # Define a prompt to ask a question
# prompt = "What is the capital of France?"

# # Generate a response using the GPT-3 language model
# response = openai.Completion.create(
#     engine="davinci",
#     prompt=prompt,
#     max_tokens=1024,
#     n=1,
#     stop=None,
#     temperature=0.5,
# )

# # Print the response
# print(response.choices[0].text.strip())


