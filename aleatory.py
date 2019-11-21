from cache import AbstractImplementation
import random


class Aleatory(AbstractImplementation):

    def __init__(self, cache_size: int):
        super().start(cache_size)

    def substitution_algorithm(self, item: str):
        index = random.randint(0, self.cache_size - 1)
        self.substitute(index, item)
