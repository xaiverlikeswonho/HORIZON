# HORIZON — Stage 1 Foundation

Python Discord server-management bot with a FastAPI website dashboard.

## Included
- discord.py bot foundation
- `..` prefix commands: `..ping`, `..help`, `..prefix`
- grouped slash command: `/horizon status`
- FastAPI dashboard shell and responsive monochrome UI
- SQLite server settings and audit-event schema
- shared service layer and action registry

This is a runnable starter foundation, not a finished production dashboard. Discord OAuth login, guild selection, persistent interactive panels, and production deployment are later milestones.

## Setup
1. Use Python 3.11 or newer.
2. Create a virtual environment: `python -m venv .venv`
3. Activate it and run: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and add your Discord bot token.
5. Run the bot: `python main.py`
6. In another terminal run: `uvicorn horizon.web:app --reload`
7. Open `http://127.0.0.1:8000`.

Enable **Message Content Intent** in the Discord Developer Portal for prefix commands. Invite with `bot` and `applications.commands` scopes. Do not grant Administrator unless truly required.

## 1,000-action design
The project target is 500 slash actions + 500 prefix actions. These are action-registry entries, not 500 separate top-level slash registrations. Discord limits top-level application commands, so slash actions will be grouped into commands/subcommands. Both interfaces will call the same service layer.

Never commit `.env` or share your bot token.
