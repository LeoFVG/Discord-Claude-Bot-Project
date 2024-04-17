import anthropic
import os

def submit_prompt(prompt: str) -> str:

    client = anthropic.Anthropic(
        # Change os.environ.get("ANTHROPIC_API_KEY") to your Anthropic_api_key if api_key is not in environment variables
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
    )
    
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
    return message.content[0].text

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    
    if lowered == "":
        return "Message cannot be empty"
    elif lowered[0] == "#":
        return submit_prompt(lowered[1:])
    
    else:
        return """Sorry im not familiar with that command, right now my only command is (#claude question)"""
