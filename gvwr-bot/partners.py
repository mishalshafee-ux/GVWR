import discord
from discord.ext import commands

DASH_EMOJI = "<:dot:1556723325009666068>"
ARROW_EMOJI = "<:arrow:1556723141630230589>"


class Partners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="partner0-20")
    @commands.has_permissions(administrator=True)
    async def partner_0_20(self, ctx):
        await ctx.send(
            f"{DASH_EMOJI} **0-20 Members** {ARROW_EMOJI} "
            f"You get no ping, we get here ping. "
        )

        try:
            await ctx.message.delete()
        except discord.HTTPException:
            pass

    @commands.command(name="partner21-50")
    @commands.has_permissions(administrator=True)
    async def partner_21_50(self, ctx):
        await ctx.send(
            f"{DASH_EMOJI} **21-50 Members** {ARROW_EMOJI} "
            f"You get here ping, we get everyone ping."
        )

        try:
            await ctx.message.delete()
        except discord.HTTPException:
            pass

    @commands.command(name="partner51")
    @commands.has_permissions(administrator=True)
    async def partner_51(self, ctx):
        await ctx.send(
            f"{DASH_EMOJI} **51+ Members** {ARROW_EMOJI} "
            f"You get everyone ping, we get everyone ping."
        )

        try:
            await ctx.message.delete()
        except discord.HTTPException:
            pass


async def setup(bot):
    await bot.add_cog(Partners(bot))
