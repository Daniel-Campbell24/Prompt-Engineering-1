import openai
from prompt import main_prompt

# Set up your OpenAI API credentials
openai.api_key = ''

# Define a function to generate a model response given a user prompt and conversation history
def generate_response(prompt):
    # Call the OpenAI API to generate a response using the provided prompt and conversation history
    response = openai.Completion.create(
        engine='text-davinci-003',  # Choose the engine you want to use
        prompt=prompt,
        max_tokens=100,  # Adjust the length of the response as needed
        temperature=0.7,  # Control the randomness of the response
        n=1,  # Generate a single response
        stop=None,  # Stop generation at a specific token
        timeout=None  # Set a timeout for the API call
    )

    if response.choices:
        return response.choices[0].text.strip()  # Return the generated response
    else:
        return ''  # Return an empty string if no response is generated

# Main loop for interacting with the model
conversation = []  # Initialize an empty list to store the conversation history

# Write the initial prompt
initial_prompt = main_prompt  # Load the prompt from the separate file
conversation.append({'role': 'system', 'content': initial_prompt})

while True:
    user_input = input("User: ")  # Get user input
    conversation.append({'role': 'system', 'content': 'You: ' + user_input})  # Add user input to the conversation as a system message

    prompt = ""
    for message in conversation:
        if message['role'] == 'system':
            prompt += message['content'] + '\n'
        else:
            prompt += message['role'] + ': ' + message['content'] + '\n'

    response = generate_response(prompt)  # Generate a response using the prompt and conversation history
    print(f"ChatGPT: {response}")  # Print the generated response

    conversation.append({'role': 'assistant', 'content': response})  # Add the generated response to the conversation history as an assistant message
