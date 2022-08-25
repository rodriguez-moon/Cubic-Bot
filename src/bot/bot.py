import os

import discord
from discord.ext import commands
from discord.ext.commands import is_owner

# from .classes import DatabaseManager
from utils import toolkit as tk


class CubicBot(commands.Bot):
    def __init__(self, config: dict):
        self.config = config
        self.version = "1.0.0"
        self.cog_list = (
            "example1", # cogs/example1.py
            "example2", # cogs/example2.py
            "example3", # cogs/example3.py
        )

        super().__init__(
            reconnect=True,
            help_command=None,
            intents=discord.Intents(
                bans=True,
                guilds=True,
                members=True,
                messages=True,
                reactions=True,
                webhooks=True,
            ),
            owner_ids=config["owners"],
            status=discord.Status.idle, # idle moon :)
            allowed_mentions=discord.AllowedMentions(everyone=False),
        )

        for cog in self.cog_list:
            self.load_extension(f"cogs.{cog}")

        # unused database & cogs implementation
        """
        if not os.path.isdir("./data"):
            os.makedirs("./data")
        self.db = DatabaseManager("./data")
        """

    async def on_ready(self):
        await self.change_presence(activity=discord.Game(f"/help!"))
        print(f"{tk.get_time()} Watching {len(self.guilds):,} servers as {self.user}")

    async def on_connect(self):
        print(f"{tk.get_time()} Connected to discord.com")

    async def on_disconnect(self):
        print(f"{tk.get_time()} Disconnected from discord.com")

    async def on_resume():
        print(f"{tk.get_time()} Reconnected to discord.com")

    async def on_message(self, message):
        if message.guild is None:
            return
        await self.process_commands(message)

    @discord.slash_command()
    async def ping(self, ctx):
        await ctx.respond("Pong!")

    @discord.slash_command(name="reload", description="Reloads all command extensions")
    @is_owner()
    async def reload_cogs(self, ctx: discord.ApplicationContext) -> None:
        for cog in dict(self.extensions):
            self.unload_extension(cog)
        for cog in self.cog_list:
            self.load_extension(f"cogs.{cog}")
        await ctx.respond(f"> Successfully reloaded extensions", ephemeral=True)
