from hashmap import HashMap


def testHashMap():

    # helper functions

    def add(key, value):
        return hashmap.set(key, value)

    def load():
        return hashmap.load()

    def delete(key):
        return hashmap.delete(key)

    def get(key):
        return hashmap.get(key)

    def test(condition):
        if condition is True:
            print("SUCCESS!")
        else:
            print("FAIL :(")

    def assert_load(number):
        print("Checking that load() is equal to {}...".format(number), end='')
        test(load() == number)

    print("Initializing hash map...")
    hashmap = HashMap(64)

    print("Checking that load() == 0...", end='')
    test(load() == 0)

    # add 10 key/value pairs to the hash map via set()
    # increment the key (int) and the value (char) by 1 each time so they're unique
    testkey = 0
    testvalue = "a"
    while testkey < 10:
        print("Adding {} of 10 pairs to the hashmap...".format(testkey + 1), end='')
        test(add(testkey, testvalue) is True)
        testkey += 1
        testvalue = chr(ord(testvalue) + 1)

    # check that our load (10/64) is equal to what it should be
    assert_load(.15625)

    # now let's test the get function
    testkey = 0
    testvalue = "a"
    while testkey < 10:
        print("Checking that get({}) returns {}...".format(testkey, testvalue), end='')
        test(get(testkey) == testvalue)
        testkey += 1
        testvalue = chr(ord(testvalue) + 1)

    # check to see if we get null on using get() for an invalid key
    print("Checking to see if we get null on an invalid key...", end='')
    test(get("Vader") is None)

    # check to see if we get null on using delete() for an invalid key
    print("Checking to see if we get null on an invalid key...", end='')
    test(delete("barnacles") is None)

    # check to see if we can delete keys 0-4 via delete function
    testkey = 0
    testvalue = "a"
    while testkey < 5:
        print("Deleting {} of 5 key/value pairs...".format(testkey + 1), end='')
        test(delete(testkey) == testvalue)
        testkey += 1
        testvalue = chr(ord(testvalue) + 1)

    # check to see if load is equal to .078125 (5 of 64 buckets)
    assert_load(.078125)

    print("Tests done!")

if __name__ == "__main__":
    testHashMap()
