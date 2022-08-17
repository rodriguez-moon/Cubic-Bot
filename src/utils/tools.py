import logging
from datetime import datetime
from os import makedirs
from os.path import abspath, isdir, join, pardir

import discord


class Toolkit:
    def __init__(self) -> None:
        self.root = abspath(join(__file__, pardir, pardir))

    def start_logging(self) -> None:
        """verbose logging saved to 'src/logs/discord.log'
        """
        log_folder = join(self.root, "logs")
        if not isdir(log_folder):
            makedirs(log_folder)

        path = join(log_folder, "discord.log")
        logger = logging.getLogger("discord")
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(filename=path, encoding="utf-8", mode="w")
        handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
        logger.addHandler(handler)

    @staticmethod
    def get_time() -> str:
        current_date = datetime.now()
        formatted = current_date.strftime("[%d/%m/%Y %H:%M:%S]")
        return formatted

    @staticmethod
    def get_intents(intents=discord.Intents.all()) -> discord.Intents:
        """intents give discord bots access to many aspects of discord.
        however, some intents may never even be used by a bot.
        this function allows the user to have full control over bot intents.
        you can read the documentation here:
        https://discord.com/developers/docs/topics/gateway#list-of-intents

        :param intents: intents object used to define a bot's gateway intents, defaults to discord.Intents.all()
        :type intents: discord.Intents, optional
        :return: returns configured gateway intents object
        :rtype: discord.Intents
        """
        intents.auto_moderation_configuration = False  # create, update, & delete auto-moderation rules
        intents.auto_moderation_execution = False  # execute auto-moderation actions
        intents.bans = True  # add & remove bans
        intents.dm_messages = True  # create, update, & delete direct messages & pins
        intents.dm_reactions = True  # add & remove reaction emojis from direct message
        intents.dm_typing = False  # recieve direct message typing events
        intents.emojis = False  # update emojis
        intents.emojis_and_stickers = False  # update emojis & stickers
        intents.guild_messages = True  # create, update, & delete (bulk) guild messages
        intents.guild_reactions = True  # add & remove reaction emojis from guild message
        intents.guild_typing = False  # recieve member typing events
        intents.guilds = True  # create, update, & delete guilds, roles, channels, pins, threads, & stage instances
        intents.integrations = True  # create, update, & delete integrations
        intents.invites = False  # create & delete invites
        intents.members = True  # [privileged] add, update, & remove members
        intents.message_content = False  # [privileged] access content, attachments, embeds, & components of messages
        intents.messages = True  # create, update, & delete messages
        intents.presences = False  # [privileged] access member presence updates
        intents.reactions = True  # add & remove emoji reactions from message
        intents.scheduled_events = False  # create, update, & delete scheduled events; add & remove users from event
        intents.typing = False  # recieve typing events
        intents.voice_states = False  # update voice states
        intents.webhooks = True  # update webhooks
        # overrides:
        # intents.all()
        # intents.default()
        # intents.none()
        return intents


if __name__ == "__main__":
    print("You're not supposed to run this file! Run main.py instead.")
