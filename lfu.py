from cache import AbstractImplementation


class Lfu(AbstractImplementation):

    def __init__(self, cache_size: int):
        super().start(cache_size)
        self.__pointer = 0

    def process(self, item: str):
        key = self.check_cache(item)
        if key is None:
            self.insert_into_cache(item)
        else:
            self.hit += 1
            self.cache_index[key][-1][1] += 1

    def substitution_algorithm(self, item: str):
        d = {}
        key = 0
        value = 1
        e = {}
        for key, lines in self.cache_index.items():
            d[key] = lines[-1]
        for k, v in d.items():
            if v[-1] <= value:
                value = v[-1]
        for k, v in d.items():
            if v[-1] == value:
                e[k] = v
        if len(e.keys()) > 1:
            while True:
                if self.__pointer == self.cache_size:
                    self.__pointer = 0
                if e.get(self.__pointer):
                    index = self.__pointer
                    self.__pointer += 1
                    break
                self.__pointer += 1
        else:
            index = [v for v in e.keys()][0]
        self.substitute(index, [item, 0])
