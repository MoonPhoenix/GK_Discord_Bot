import discord
from discord.ext import commands

TOKEN = 'NzAwMDUyODAzMzg4NzAyODUz.XpdgmA.R2Qrsm8do47i2anxb3pxz6OQOxI'

BOTPERMISSION = 133184

class BotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))
    async def on_disconnect(self):
        print('Disconnecting!')
    async def on_message(self, message):
        if(message.author == self.user):
            return
        if(message.content == 'ping'):
            msg = 'Ping Received by {0.author.mention}'.format(message)
            await message.channel.send(msg)

client = BotClient()
client.run(TOKEN)