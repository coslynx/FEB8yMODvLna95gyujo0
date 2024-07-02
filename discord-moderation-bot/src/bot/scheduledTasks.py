import discord
import asyncio

class ScheduledTasks:
    def __init__(self, client):
        self.client = client

    async def clear_chat_history(self, channel_id):
        channel = self.client.get_channel(channel_id)
        if channel:
            await channel.purge(limit=None)
        else:
            print("Channel not found.")

    async def update_user_roles(self, guild_id, user_id, role_id):
        guild = self.client.get_guild(guild_id)
        if guild:
            member = guild.get_member(user_id)
            if member:
                role = guild.get_role(role_id)
                if role:
                    await member.add_roles(role)
                else:
                    print("Role not found.")
            else:
                print("Member not found.")
        else:
            print("Guild not found.")

    async def scheduled_task_handler(self):
        while True:
            # Implement your scheduled tasks here
            await asyncio.sleep(60)  # Run the tasks every 60 seconds

# Run the scheduled task handler
client = discord.Client()
task = ScheduledTasks(client)

@client.event
async def on_ready():
    print('Bot is ready.')
    client.loop.create_task(task.scheduled_task_handler())

client.run('your_token_here')