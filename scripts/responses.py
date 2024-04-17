# Importing necessary modules
import anthropic
import os

# Function to submit a prompt to the Anthropic API
def submit_prompt(prompt: str) -> str:
    # Initialize the Anthropic client with your API key
    client = anthropic.Anthropic(
        # Change os.environ.get("ANTHROPIC_API_KEY") to your Anthropic_api_key if api_key is not in environment variables
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
    )
    
    # Create a message with the Anthropic API
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )
    # Return the text of the response
    return message.content[0].text

# Function to get a response based on user input
def get_response(user_input: str) -> str:
    # Convert the user input to lowercase
    lowered: str = user_input.lower()
    
    # Check if the user input is empty
    if lowered == "":
        return "Message cannot be empty"
    # Check if the user input starts with "#"
    elif lowered[0] == "#":
        # Submit the prompt to the Anthropic API
        return submit_prompt(lowered[1:])
    
    else:
        # Return a default response if the command is not recognized
        return """Sorry im not familiar with that command, right now my only command is (#claude question)"""
