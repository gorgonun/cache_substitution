from cache import AbstractImplementation


class Lru(AbstractImplementation):

    def __init__(self, cache_size: int):
        super().start(cache_size)

    def process(self, item: str):
        key = self.check_cache(item)
        if key is None:
            self.insert_into_cache(item)
        else:
            self.hit += 1
        for k in self.cache_index.keys():
            self.cache_index[k][-1][1] += 1
        if key is not None:
            self.cache_index[key][-1][1] = 0

    def substitution_algorithm(self, item: str):
        d = {}
        key = 0
        value = 0
        for key, lines in self.cache_index.items():
            d[key] = lines[-1]
        for k, v in d.items():
            if v[-1] >= value:
                value = v[-1]
        for k, v in d.items():
            if v[-1] == value:
                key = k
        self.substitute(k, [item, 0])
