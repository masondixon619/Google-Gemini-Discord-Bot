import discord
from google import genai

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('!ask'):
            prompt = message.content[5:]  # Remove the '!ask' part
            response = generate_genai_response(prompt)
            await message.channel.send(f'Here is your response {message.author}: {response}')
                

def generate_genai_response(prompt):
    
    client = genai.Client(api_key= '') # Add your Gemini API key here

    response = client.models.generate_content(
    model="gemini-2.0-flash", contents = prompt
    )

    return response.text
        



intents = discord.Intents.default()
intents.message_content = True


client = Client(intents=intents)
client.run('') # Add your Discord bot token here
