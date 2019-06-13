from discord.ext import commands

class tools(commands.Cog):

    @commands.command(name='countdown', aliases=['fuck'])
    async def _search(self, ctx, *, seconds):
    """
    Counts down <seconds> seconds
    """
    
def setup(bot):
    bot.add_cog(Cogs(bot))
