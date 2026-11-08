from horizon.database import connection

async def get_prefix(guild_id: int) -> str:
    with connection() as db:
        row = db.execute("SELECT prefix FROM guild_settings WHERE guild_id=?", (guild_id,)).fetchone()
        if row:
            return row["prefix"]
        db.execute("INSERT OR IGNORE INTO guild_settings (guild_id, prefix) VALUES (?, '..')", (guild_id,))
        return ".."

async def set_prefix(guild_id: int, prefix: str) -> None:
    with connection() as db:
        db.execute("INSERT INTO guild_settings (guild_id, prefix, updated_at) VALUES (?, ?, CURRENT_TIMESTAMP) ON CONFLICT(guild_id) DO UPDATE SET prefix=excluded.prefix, updated_at=CURRENT_TIMESTAMP", (guild_id, prefix))
