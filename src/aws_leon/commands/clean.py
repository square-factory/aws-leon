from dataclasses import dataclass


@dataclass
class Cleaner:

    def __init__(self):
        pass

    def execute(self):
        return "cleaned"
