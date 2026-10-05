import discord
from discord.ext import commands

GVWR_AD_MESSAGE = """
# Greenville Worldwide Roleplay Community — *"The Future of Roleplays"*

Ever wanted to Roleplay with people who **don't** break the law? Well then, you've found the right Roleplay for you, **Greenville Worldwide Roleplay Community!**

— What we need:

> Active Staff
> Active Roleplayers
> Awesome Partners

So what you waiting for? Join the action today at [Greenville Worldwide Roleplay Community](https://discord.gg/yps5DZE824)
"""


class Advertisements(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="GVWRad", aliases=["gvrnad"])
    @commands.check(lambda ctx: ctx.author.guild_permissions.administrator or any(role.id == 1531256052593459240 for role in ctx.author.roles))
    async def gvrn_ad(self, ctx):
        await ctx.send(GVWR_AD_MESSAGE)

        try:
            await ctx.message.delete()
        except discord.HTTPException:
            pass


async def setup(bot):
    await bot.add_cog(Advertisements(bot))
