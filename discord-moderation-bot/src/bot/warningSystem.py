import discord

class WarningSystem:
    def __init__(self):
        self.warnings = {}

    async def issue_warning(self, user_id, reason):
        if user_id not in self.warnings:
            self.warnings[user_id] = []
        self.warnings[user_id].append(reason)

    async def get_warnings(self, user_id):
        if user_id in self.warnings:
            return self.warnings[user_id]
        return []

    async def clear_warnings(self, user_id):
        if user_id in self.warnings:
            del self.warnings[user_id]

    async def check_warnings_threshold(self, user_id, threshold):
        if user_id in self.warnings and len(self.warnings[user_id]) >= threshold:
            return True
        return False

    async def display_warnings(self, user_id):
        warnings = await self.get_warnings(user_id)
        if warnings:
            return f"User {user_id} has {len(warnings)} warnings: {', '.join(warnings)}"
        return f"User {user_id} has no warnings"

    async def handle_warning_system(self, message):
        if message.content.startswith("!warn"):
            args = message.content.split(" ")
            if len(args) < 3:
                await message.channel.send("Invalid command usage. Try !warn @user <reason>")
                return
            user_id = args[1]
            reason = " ".join(args[2:])
            await self.issue_warning(user_id, reason)
            await message.channel.send(f"Warning issued to {user_id} for: {reason}")

# Create an instance of the WarningSystem class
warning_system = WarningSystem()