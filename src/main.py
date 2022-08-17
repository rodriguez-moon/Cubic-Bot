import discord

from bot import CubicBot
from utils import toolkit as tk


def main() -> None:
    tk.start_logging()
    bot = CubicBot(
        reconnect=True,
        help_command=None,
        intents=tk.get_intents(),
        status=discord.Status.idle, # idle moon :)
        allowed_mentions=discord.AllowedMentions(everyone=False),
    )

    bot_token = "BOT_TOKEN"
    bot.run(bot_token)


if __name__ == "__main__":
    main()
