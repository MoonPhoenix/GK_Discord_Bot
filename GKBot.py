import discord
from discord.ext import commands

TOKEN = 'NzAwMDUyODAzMzg4NzAyODUz.XpdgmA.R2Qrsm8do47i2anxb3pxz6OQOxI'

BOTPERMISSION = 133184

class BotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))
        return
    async def on_disconnect(self):
        print('Disconnecting!')
        return
    async def on_message(self, message):
        if(message.author == self.user):
            return
        if(message.content == '!söz'):
            if message.author in UserQueue:
                msg = 'Zaten {0}. sıradasınız'.format(UserQueue.index(message.author)+1)
                await message.channel.send(msg)
                return
            msg = '{0.author.mention}\'a söz verildi, {1}. sırada'.format(message,len(UserQueue)+1)
            await message.channel.send(msg)
            UserQueue.append(message.author)
            return
        if(message.content == "!pop"):
            for i in message.author.roles:
                if i.name in ['DK', 'YK', 'MOD']:
                    if (len(UserQueue) == 0):
                        msg = 'Sırada kimse yok'.format()
                        await message.channel.send(msg)
                        return
                    msg = '{0.mention}\'ın söz hakkı'.format(UserQueue.pop(0))
                    await message.channel.send(msg)
                    return
            msg = 'Bu komutu kullanmak için yetkiniz yok'
            await message.channel.send(msg)
            return
UserQueue = []
client = BotClient()
client.run(TOKEN)
