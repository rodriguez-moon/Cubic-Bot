from .bot import CubicBot
from utils import toolkit as tk

print(f"{tk.get_time()} Initialised bot module")

# only impacts 'from bot import *'
__all__ = ["CubicBot"]
