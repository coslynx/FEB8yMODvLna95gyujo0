import discord

class CommandHandler:
    def __init__(self, client):
        self.client = client

    async def handle_command(self, message):
        if message.content.startswith('!kick'):
            await self.kick_user(message)
        elif message.content.startswith('!ban'):
            await self.ban_user(message)
        elif message.content.startswith('!mute'):
            await self.mute_user(message)
        else:
            await message.channel.send('Invalid command. Please try again.')

    async def kick_user(self, message):
        if message.author.guild_permissions.kick_members:
            try:
                member = message.mentions[0]
                await member.kick()
                await message.channel.send(f'{member.mention} has been kicked.')
            except:
                await message.channel.send('Unable to kick the user.')
        else:
            await message.channel.send('You do not have permission to kick users.')

    async def ban_user(self, message):
        if message.author.guild_permissions.ban_members:
            try:
                member = message.mentions[0]
                await member.ban()
                await message.channel.send(f'{member.mention} has been banned.')
            except:
                await message.channel.send('Unable to ban the user.')
        else:
            await message.channel.send('You do not have permission to ban users.')

    async def mute_user(self, message):
        if message.author.guild_permissions.manage_roles:
            try:
                member = message.mentions[0]
                mute_role = discord.utils.get(message.guild.roles, name='Muted')
                await member.add_roles(mute_role)
                await message.channel.send(f'{member.mention} has been muted.')
            except:
                await message.channel.send('Unable to mute the user.')
        else:
            await message.channel.send('You do not have permission to mute users.')

# Instantiate the CommandHandler class and pass the client instance
def setup(client):
    client.add_cog(CommandHandler(client))