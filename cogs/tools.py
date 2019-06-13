from discord.ext import commands

class tools(commands.Cog):

    @commands.command(name='countdown', aliases=['fuck'])
    async def _search(self, ctx, time: int = 5, *, string):
    """
    Counts down until movie
    """
    for i in range(time):
            remaining = time - i
            await asyncio.sleep(1)
            if remaining <= 5:
                await ctx.send(remaining)
            elif remaining % 5 == 0 and remaining < 60:
                await ctx.send(remaining)
            elif remaining % 60 == 0:
                await ctx.send(f'{remaining//60} min')

        await asyncio.sleep(1)
        await ctx.send(string)
    
def setup(bot):
    bot.add_cog(Cogs(bot))
