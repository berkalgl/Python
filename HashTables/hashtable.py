class HashTable:
    def __init__(self, size):
        self.data = [None] * size
    
    def _hash(self, key):
        hash = 0
        for i in range(0, len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash

    def set(self, key, value):
        address = self._hash(key)
        print(address)
        if self.data[address] == None:
            self.data[address] = []        
        self.data[address].append([key,value])
        print(self.data)

    def get(self, key):
        address = self._hash(key)
        currentBucket = self.data[address]
        if currentBucket and len(currentBucket) > 0:
            for array in currentBucket:
                if array[0] == key:
                    return array[1]
        
        return 'Key could not be found'

    def keys(self):
        keys = []
        for array in self.data:
            if array:
                keys.append(array[0][0])
        return keys
        
#can override the data in hash that is called collision
hashTable = HashTable(50)
hashTable.set('grapes', 10000)
hashTable.set('apples', 10000)
print(hashTable.get('grapes'))
print(hashTable.get('apples'))
print(hashTable.keys())
