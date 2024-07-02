import discord

class Logs:
    def __init__(self, client):
        self.client = client

    async def log_moderation_action(self, action_type, user, reason):
        log_channel = discord.utils.get(user.guild.text_channels, name='mod-logs')
        if log_channel:
            await log_channel.send(f'{action_type} - {user.name}#{user.discriminator} - {reason}')
        else:
            print('Error: Mod-logs channel not found.')

    async def log_warning(self, user, reason):
        await self.log_moderation_action('Warning', user, reason)

    async def log_mute(self, user, reason):
        await self.log_moderation_action('Mute', user, reason)

    async def log_kick(self, user, reason):
        await self.log_moderation_action('Kick', user, reason)

    async def log_ban(self, user, reason):
        await self.log_moderation_action('Ban', user, reason)