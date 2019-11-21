from abc import ABC, abstractmethod


class AbstractImplementation(ABC):

    @abstractmethod
    def __init__(self, cache_size: int):
        pass

    def start(self, cache_size):
        self.cache_size = cache_size
        self.cache_index = {}
        self.hit = 0
        self.compulsory_miss = 0
        self.conflict_miss = 0

    def process(self, item: str):
        key = self.check_cache(item)
        if key is None:
            self.insert_into_cache(item)
        else:
            self.hit += 1

    def check_cache(self, item: str):
        d = self.valueDict()
        for key, value in d.items():
            if item == value[-1]:
                return key

    @abstractmethod
    def substitution_algorithm(self, item: str):
        pass
    
    def substitute(self, index: int, item: str):
        old_item = self.cache_index[index][-1]
        self.cache_index[index].append(item)

    def insert_into_cache(self, item: str):
        space = len(self.cache_index.keys())
        if space == self.cache_size:
            self.miss(item)
            self.substitution_algorithm(item)
        else:
            return self.append_to_cache(item)

    def append_to_cache(self, item: str):
        index = len(self.cache_index.keys())
        self.cache_index[index] = [[item, 0]]
        self.compulsory_miss += 1
        
    def substitute_in_cache(self, old_item: str, index: int, item: str):
        self.cache_index[index] += [item, 0]
    
    def miss(self, item):
        d = self.valueDict()
        if item not in [value for values in d.values() for value in values]:
            self.compulsory_miss += 1
        else:
            self.conflict_miss += 1
    
    def valueDict(self):
        d = {}
        for key, lines in self.cache_index.items():
            d[key] = []
            for value in lines:
                d[key].append(value[0])
        return d

    def __str__(self):
        layout = "{:<5}|{}"
        title = layout.format("index", "items")
        result = "\n".join([
            "Hit: {}".format(self.hit),
            "Compulsory miss: {}".format(self.compulsory_miss),
            "Conflic miss: {}".format(self.conflict_miss)
            ])
        d = self.valueDict()
        return "\n" + "\n".join([title] + [layout.format(key, ", ".join(value)) for key, value in d.items()] + [result])
        