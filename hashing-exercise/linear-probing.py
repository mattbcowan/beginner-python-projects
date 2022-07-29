class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None] * self.MAX

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    # Overriding Operators
    def __setitem__(self, key, val):
        hash = self.get_hash(key)
        if self.arr[hash] is None:
            self.arr[hash] = (key, val)
        else:
            for i in range(len(self.arr)):
                if self.arr[i] is None:
                    self.arr[i] = (key, val)
                    break

    def __getitem__(self, key):
        pass

    def __delitem__(self, key):
        pass


t = HashTable()
t["march 6"] = 130
t["march 9"] = 459
t["march 17"] = 20
t["march 21"] = 27

print(t.arr)
