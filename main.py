# Importing necessary modules
from typing import Final
from scripts.responses import get_response
from discord import Intents, Client, Message

# Your discord bot token
TOKEN = "(your discord bot token here)"

# Setting up intents for the bot
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

# Function to send message
async def send_message(message: Message, user_message: str) -> None:
    # Check if the message is empty
    if not user_message:
        print("(Message was empty, most likely intents were not enabled)")
    # Check if the message is private
    if is_private := user_message[0] == "?":
        user_message = user_message[1:]
    
    try:
        # Get response for the user message
        response: str = get_response(user_message)
        # Send response to the user
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# Event for when the bot is ready
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running!")

# Event for when a message is received
@client.event
async def on_message(message: Message) -> None:
    # Ignore messages from the bot itself
    if message.author == client.user:
        return
    
    # Get username and message content
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    # Print the message details
    print(f"[{channel}] {username}: {user_message}")
    # Send a response to the message
    await send_message(message, user_message)

# Main function to run the bot
def main() -> None:
    client.run(token=TOKEN)

# Run the main function
if __name__ == "__main__":
    main()
