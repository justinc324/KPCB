class HashMap:
    # initialize the hashmap, let parameter set size of hashmap
    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size
        self.items = 0

    def set(self, key, value):
        # creates a list
        key_value_pair = [key, value]

        # determine which bucket of the array we are going to drop the key/value pair in, using hash
        bucket = self.get_hash(key)

        # If the index is empty, drop it in. Else, check to see if the key exists in the current bucket
        # if it exists, update value; else, append it
        if self.check_hashmap(key):
            self.map[bucket] = list([key_value_pair])
            self.items += 1
            return True
        else:
            for pair in self.map[bucket]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[bucket].append(key_value_pair)
        return False

    def get(self, key):
        # see where it would have been hashed
        bucket = self.get_hash(key)

        # if that bucket is empty, return none(null)
        if self.check_hashmap(key):
            return None
        # else, if bucket is not empty, check through bucket for key. If key is there, return the value - else return
        # None
        else:
            for pair in self.map[bucket]:
                if pair[0] == key:
                    return pair[1]
            return None

    def delete(self, key):
        bucket = self.get_hash(key)

        # if key's bucket is empty, return None. Else check the bucket for the key - if there delete the value and
        # return it. Else return None
        if self.check_hashmap(key):
            return None
        else:
            # probe through pairs in bucket, pop off bucket if it has corresponding key
            i = 0
            for pair in self.map[bucket]:
                if pair[0] == key:
                    deleted_item = pair[1]
                    self.map[bucket].pop(i)
                    if len(self.map[bucket]) > 1:
                        for i in self.map[bucket]:
                            if len(self.map[bucket][i]) > 0 is False:
                                self.items -= 1
                    else:
                        self.items -= 1
                    return deleted_item
                i += 1
            return None

    # returns the load factor on the hash map
    def load(self):
        return self.items / self.size

    # helper functions

    # check to see if the given key's bucket is empty(returns True) or not(returns false)
    def check_hashmap(self, key):
        bucket = self.get_hash(key)

        if self.map[bucket] is None:
            return True
        else:
            return False

    # returns the appropriate bucket (array) for an item
    def get_hash(self, key):
        return hash(key) % self.size





