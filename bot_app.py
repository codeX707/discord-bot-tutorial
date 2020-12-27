import discord

intents = discord.Intents.default()
intents.members = True


def get_token():
    with open("config.txt", "r") as config_file:
        token_line = config_file.readlines()[0]
        token = token_line.split(" ")[1]
        return token


TOKEN = get_token()

client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    server_id = 792768885073117195  # id serwera
    server = client.get_guild(server_id)
    if "czesc" in message.content:
        await message.channel.send("Witaj!")

    if "!uzytkownicy" in message.content:
        await message.channel.send("Liczba użytkowników na serwerze: " + str(server.member_count))


@client.event
async def on_member_join(member):
    welcome_channel_id = 792775001295945769  # id kanału z powitaniami
    await client.get_channel(welcome_channel_id).send(member.mention + " witaj na serwerze!",
                                                      file=discord.File("assets/hello.jpg"))


client.run(TOKEN)
