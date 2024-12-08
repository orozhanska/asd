class Node:
    """
    A Node in the linked list used for chaining.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.elcount = 0
        self.buckets = [None] * self.size  # Output: [None, None, None, None, None]

    # TODO: 1. Implement the _hash_function method. Use your custom hashing function from Task #1.
    def _hash_function(self, key):
        output = sum([ord(x) for x in key]) % self.size
        return output
    
    # TODO: 2. Implement the insert_or_update method. It should insert a new 
    # key-value pair or update the value if the key already exists.

    def insert_or_update(self, key, value):
        index = self._hash_function(key)
        head = self.buckets[index]

        current = head
        while current:
            if current.key == key:
                current.value = value  
                return
            current = current.next

        new_node = Node(key, value)
        new_node.next = head
        self.buckets[index] = new_node
        self.elcount +=1

    def search(self, key):
        index = self._hash_function(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self._hash_function(key)
        current = self.buckets[index]
        prev = None
        while current:
            if current.key == key:
                self.elcount -= 1
                if prev:
                    prev.next = current.next
                else:
                    self.buckets[index] = current.next
                return True
            prev = current
            current = current.next
        return False

    # TODO: 3. Implement the display method. It should display the contents of the hashtable.
    
    def display(self):
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}:", end=" ")
            current = bucket
            while current:
                print(f"({current.key}, {current.value}) ->", end=" ")
                current = current.next
            print("None")

    # TODO: 4. Implement the number_of_elements method. It should return the total number of elements in the hashtable.
    
    def number_of_elements(self):
        return self.elcount


if __name__ == "__main__":
    ht = HashTable(5)  # Create a hashtable with 5 slots

    # Insert key-value pairs
    ht.insert_or_update("GOOGL", 1430.79)
    ht.insert_or_update("ARMKAV", 0.59)
    ht.insert_or_update("PZTHTA", 1860.84)
    ht.insert_or_update("MNBNK", 100.00)
    ht.insert_or_update("KSECOIN", 100000.50)
    assert ht.number_of_elements() == 5

    # Display the hashtable
    print("Hashtable contents:")
    ht.display()

    # Search for a key
    assert ht.search("GOOGL") == 1430.79, "Test case 1 failed"
    assert ht.search("ARMKAV") == 0.59, "Test case 2 failed"
    assert ht.search("PZTHTA") == 1860.84, "Test case 3 failed"
    assert ht.search("MNBNK") == 100.00, "Test case 4 failed"
    assert ht.search("OBLNK") is None, "Test case 5 failed"  # Key not in table
    assert ht.search("ksecoin") is None, "Test case 6 failed"  # Key not in table, case-sensitive

    # Delete a key
    assert ht.delete("ARMKAV") is True, "Test case 7 failed"
    assert ht.delete("OBLNK") is False, "Test case 8 failed"  # Key not in table
    assert ht.number_of_elements() == 4

    # Display the hashtable after deletion
    print("\nHashtable contents after deletion:")
    ht.display()

    # Updating values
    #
    # Because you solved the first 2 homeworks, stocks are up, you are rich now!
    ht.insert_or_update("KSECOIN", 200000.50)
    # Since you are rich now, you no longer visiting Puzata Hata, so their stock price is 0.0 :(
    ht.insert_or_update("PZTHTA", 0.0)
    assert ht.number_of_elements() == 4

    # Display the hashtable after update
    print("\nHashtable contents after update:")
    ht.display()

    print("\033[92mAll test cases passed\033[0m")
