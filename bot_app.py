import discord


def get_token():
    with open("config.txt", "r") as config_file:
        token_line = config_file.readlines()[0]
        token = token_line.split(" ")[1]
        return token


TOKEN = get_token()

client = discord.Client()


@client.event
async def on_message(message):
    if "czesc" in message.content:
        await message.channel.send("Witaj!")


client.run(TOKEN)
