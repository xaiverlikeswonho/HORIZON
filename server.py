from discord.ext import commands
from horizon.services.guild_settings import set_prefix

class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="prefix")
    @commands.guild_only()
    @commands.has_guild_permissions(manage_guild=True)
    async def prefix_command(self, ctx, new_prefix: str):
        if not 1 <= len(new_prefix) <= 5 or any(ch.isspace() for ch in new_prefix):
            await ctx.reply("Prefix must be 1–5 non-space characters.", mention_author=False)
            return
        await set_prefix(ctx.guild.id, new_prefix)
        await ctx.reply(f"Prefix updated to `{new_prefix}`.", mention_author=False)

async def setup(bot):
    await bot.add_cog(Server(bot))
