from discord.ext import commands

INITIAL_COGS = ["cogs.ready", "cogs.hello"]


class Robot(commands.Bot):
    def __init__(self, command_prefix: str = "!") -> None:
        super().__init__(command_prefix=commands.when_mentioned_or(command_prefix))

        for cog in INITIAL_COGS:
            self.load_extension(cog)


if __name__ == "__main__":
    import os

    bot = Robot()
    bot.run(os.environ["DISCORD_TOKEN"])
