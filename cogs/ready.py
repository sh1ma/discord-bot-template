from discord.ext.commands import Bot, Cog


class Echo(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print("起動しました！")


def setup(bot: Bot) -> None:
    bot.add_cog(Echo(bot))
