class MyHashSet:

    def __init__(self):
        self.hash = []

    def add(self, key: int) -> None:
        self.hash.append(key)
        
    def remove(self, key: int) -> None:
        new = []
        for k in self.hash:
            if k != key:
                new.append(k)
        self.hash = new
        
        return self.hash
        

    def contains(self, key: int) -> bool:
        for k in self.hash:
            if k == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)