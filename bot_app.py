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

    if "!usun" in message.content:
        number = int(message.content.split(" ")[1])
        async for msg in message.channel.history(limit=number):
            await msg.delete()

    if "https://discord.gg" in message.content:
        await message.delete()
        await message.channel.send(message.author.mention + " reklamuje inny serwer!")
        with open("warnings.txt", "r+") as warnings_file:
            user_in_warnings = False
            warnings = warnings_file.readlines()
            for warning in warnings:
                if str(message.author) in warning:
                    await message.author.kick()
            if not user_in_warnings:
                warnings_file.write(str(message.author) + "\n")


@client.event
async def on_member_join(member):
    welcome_channel_id = 792775001295945769  # id kanału z powitaniami
    await client.get_channel(welcome_channel_id).send(member.mention + " witaj na serwerze!",
                                                      file=discord.File("assets/hello.jpg"))


client.run(TOKEN)
