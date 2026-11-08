import discord
from discord import app_commands
from discord.ext import commands

class HorizonGroup(app_commands.Group):
    def __init__(self):
        super().__init__(name="horizon", description="HORIZON bot information and controls")

    @app_commands.command(name="status", description="Check HORIZON's status")
    async def status(self, interaction: discord.Interaction):
        embed = discord.Embed(title="HORIZON Status", description="The bot is online and responding.", color=discord.Color.from_rgb(20, 20, 20))
        embed.add_field(name="Latency", value=f"{round(interaction.client.latency * 1000)} ms")
        await interaction.response.send_message(embed=embed, ephemeral=True)

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.tree.add_command(HorizonGroup())

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.reply(f"Pong! `{round(self.bot.latency * 1000)} ms`", mention_author=False)

    @commands.command(name="help")
    async def help_command(self, ctx):
        prefix = ".."
        if ctx.guild:
            from horizon.services.guild_settings import get_prefix
            prefix = await get_prefix(ctx.guild.id)
        await ctx.reply(f"**HORIZON — Starter Commands**\\n`{prefix}ping` — Check latency\\n`{prefix}help` — Show help\\n`{prefix}prefix <new>` — Change server prefix\\n`/horizon status` — Check bot status", mention_author=False)

async def setup(bot):
    await bot.add_cog(Core(bot))
