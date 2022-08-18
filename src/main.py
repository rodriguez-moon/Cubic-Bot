from bot import CubicBot
from utils import toolkit as tk


def main() -> None:
    tk.start_logging()
    config = tk.load_config()
    bot = CubicBot(config)
    bot.run(config["bot-token"])


if __name__ == "__main__":
    main()
