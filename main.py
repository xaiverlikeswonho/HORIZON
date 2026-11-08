import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv
from horizon.config import settings
from horizon.database import init_db
from horizon.services.guild_settings import get_prefix

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")
log = logging.getLogger("horizon")

async def dynamic_prefix(bot, message):
    if message.guild is None:
        return commands.when_mentioned_or(settings.bot_prefix)(bot, message)
    return commands.when_mentioned_or(await get_prefix(message.guild.id))(bot, message)

intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True  # Also enable in the Discord Developer Portal.

bot = commands.Bot(command_prefix=dynamic_prefix, intents=intents, help_command=None, case_insensitive=True)

@bot.event
async def setup_hook():
    await init_db()
    await bot.load_extension("horizon.cogs.core")
    await bot.load_extension("horizon.cogs.server")
    await bot.tree.sync()
    log.info("HORIZON commands synced")

@bot.event
async def on_ready():
    log.info("Logged in as %s", bot.user)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your server"))

if __name__ == "__main__":
    if not settings.discord_token:
        raise RuntimeError("DISCORD_TOKEN missing. Copy .env.example to .env and add your token.")
    bot.run(settings.discord_token)
