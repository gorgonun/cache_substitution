from cache import AbstractImplementation


class Fifo(AbstractImplementation):

    def __init__(self, cache_size: int):
        super().start(cache_size)
        self.__pointer = 0

    def substitution_algorithm(self, item: str):
        index = self.__pointer
        self.substitute(index, item)
        self.__pointer += 1
        if self.__pointer == self.cache_size:
            self.__pointer = 0