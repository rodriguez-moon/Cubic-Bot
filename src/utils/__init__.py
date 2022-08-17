from .tools import Toolkit

toolkit = Toolkit()

print(f"{toolkit.get_time()} Initialised utils module")

# only impacts 'from utils import *'
__all__ = ["toolkit"]
