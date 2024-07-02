import discord

class BanSystem:
    def __init__(self, client):
        self.client = client

    async def ban_user(self, user_id, reason):
        try:
            user = await self.client.fetch_user(user_id)
            await user.send(f"You have been banned from the server. Reason: {reason}")
            await self.client.ban(user, reason=reason)
            return True
        except discord.errors.NotFound:
            print("User not found.")
            return False

    async def unban_user(self, user_id):
        banned_users = await self.client.bans()
        for entry in banned_users:
            if entry.user.id == user_id:
                await self.client.unban(entry.user)
                return True
        return False

    async def check_ban_status(self, user_id):
        banned_users = await self.client.bans()
        for entry in banned_users:
            if entry.user.id == user_id:
                return True
        return False

    async def get_ban_reason(self, user_id):
        banned_users = await self.client.bans()
        for entry in banned_users:
            if entry.user.id == user_id:
                return entry.reason
        return None

    async def get_banned_users(self):
        banned_users = await self.client.bans()
        return [entry.user for entry in banned_users]