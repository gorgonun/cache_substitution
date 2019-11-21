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
        key = self.check_cache(item)
        self.cache_index[key][-1][1] = 0

    def __str__(self):
        layout = "{:<5}|{:<30}|{}"
        title = layout.format("index", "items", "usage")
        result = "\n".join([
            "Hit: {}".format(self.hit),
            "Compulsory miss: {}".format(self.compulsory_miss),
            "Conflic miss: {}".format(self.conflict_miss)
            ])
        d = {}
        usage = []
        for key, lines in self.cache_index.items():
            d[key] = []
            for value in lines:
                d[key].append(value[0])
            usage.append(lines[-1][1])
        
        return "\n" + "\n".join([title] + [layout.format(key, ", ".join(value), usage[key]) for key, value in d.items()] + [result])

    def substitution_algorithm(self, item: str):
        d = {}
        key = None
        value = 0
        for key, lines in self.cache_index.items():
            d[key] = lines[-1]
        for k, v in d.items():
            if v[-1] >= value:
                value = v[-1]
        for k, v in d.items():
            if v[-1] == value:
                key = k

        self.substitute(key, [item, 0])
