import discord

class RoleManagement:
    def __init__(self, client):
        self.client = client

    async def assign_role(self, user, role):
        try:
            await user.add_roles(role)
        except Exception as e:
            print(f"Error assigning role: {e}")

    async def remove_role(self, user, role):
        try:
            await user.remove_roles(role)
        except Exception as e:
            print(f"Error removing role: {e}")

    async def handle_user_behavior(self, user, behavior):
        if behavior == "violation":
            # Issue a warning
            await self.issue_warning(user)
            # Remove roles
            await self.remove_role(user, "Muted")
        elif behavior == "positive":
            # Assign a new role
            await self.assign_role(user, "Member")

    async def issue_warning(self, user):
        try:
            # Log the warning
            await self.log_warning(user)
            # Send a warning message
            await user.send("You have received a warning for violating server rules.")
        except Exception as e:
            print(f"Error issuing warning: {e}")

    async def log_warning(self, user):
        try:
            # Log the warning in the server
            channel = discord.utils.get(user.guild.text_channels, name="warnings-log")
            await channel.send(f"{user.name} has been warned.")
        except Exception as e:
            print(f"Error logging warning: {e}")