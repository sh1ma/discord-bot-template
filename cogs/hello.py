from discord.ext.commands import Bot, Cog, Context, command


class Hello(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @command()
    async def hello(self, ctx: Context):
        await ctx.send("hello")


def setup(bot: Bot) -> None:
    bot.add_cog(Hello(bot))
