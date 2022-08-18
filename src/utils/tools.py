import json
import logging
from datetime import datetime
from os import makedirs
from os.path import abspath, isdir, isfile, join, pardir


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

    def load_config(self) -> dict:
        file = join(self.root, "config.json")
        if not isfile(file):
            raise FileNotFoundError(
                f"Required file 'config.json' does not exist."
            )
        with open(file, "r", encoding="utf-8") as f:
            config = json.load(f)
        return config

    @staticmethod
    def get_time() -> str:
        current_date = datetime.now()
        formatted = current_date.strftime("[%d/%m/%Y %H:%M:%S]")
        return formatted


if __name__ == "__main__":
    print("You're not supposed to run this file! Run main.py instead.")
