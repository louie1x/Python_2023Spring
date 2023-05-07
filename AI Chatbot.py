import nltk
import wolframalpha
import openai
import random
import re

# Set up the OpenAI API key
openai.api_key = "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"

# Define a function to generate a response to user input1+
def generate_response(user_input, context):
    # Tokenize the user input
    tokens = nltk.word_tokenize(user_input.lower())
    # Check for a math or science question
    if any(math_word in tokens for math_word in ["calculate", "solve", "math", "equation", "formula", "science", "physics", "chemistry", "biology"]):
        # Try to answer the question using Wolfram Alpha
        try:
            # Remove any non-math words from the user input
            math_input = re.sub(r'[^\w\s+-/*^()]', '', user_input)
            # Check if the input is a simple math problem
            if any(operator in math_input for operator in ["+", "-", "*", "/", "^"]):
                # Solve the math problem using Python's eval() function
                answer = eval(math_input)
                return str(answer)
            else:
                # Query Wolfram Alpha for the math problem
                client = wolframalpha.Client("7K9HLL-WXEYKHQ3P7")
                res = client.query(math_input)
                # Get the answer from the result
                answer = next(res.results).text
                return answer
        except:
            # Return a message saying there was an error
            return "I'm sorry, there was an error while solving your math problem."
    # Check for a conversation starter
    elif any(greeting_word in tokens for greeting_word in ["hello", "hi", "hey", "what's up", "howdy"]):
        # Generate a random greeting response
        greeting_responses = ["Hello!", "Hi there!", "Hey!", "What's up?", "Howdy!"]
        return random.choice(greeting_responses)
    # Check for a farewell
    elif any(farewell_word in tokens for farewell_word in ["goodbye", "bye", "see you", "later"]):
        # Generate a random farewell response
        farewell_responses = ["Goodbye!", "See you later!", "Farewell!", "Take care!"]
        return random.choice(farewell_responses)
    # Check for a question about a topic
    else:
        # Try to answer the question using OpenAI's GPT-3 language model
        try:
            # Generate a response using the model
            prompt = f"{context}\nUser: {user_input}\nAI:"
            response = openai.Completion.create(
                engine="davinci",
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
                api_key="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"
            )
            # Get the text of the response
            text = response.choices[0].text.strip()
            # Remove any trailing newline characters
            text = text.replace("\n", " ")
            # Return the response
            return text
        except:
            # Return a message saying there was an error
            return "I'm sorry, there was an error while processing your question."

# Start the chatbot
print("Hello! I'm an AI chatbot. How can I help you?")
context = ""
while True:
    user_input = input("> ")
    if user_input.lower() == "quit":
        break
    response = generate_response(user_input, context)
    print(response)
    context += f"\nUser: {user_input}\nAI: {response}"
