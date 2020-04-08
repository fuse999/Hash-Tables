# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.size = 0
        self.old_size = None


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        '''

        index = self._hash_mod(key)# Get hash
        node = self.storage[index]
        # if it is not, then the node pointer will point to the current's next node
        while node is not None and node.key != key:
            node = node.next
        if node is not None:# then I check if it is empty
            node.value = value
        else:
            new_node = LinkedPair(key, value)
            # if it is, we create the node on that index and return
            new_node.next = self.storage[index]
            self.storage[index] = new_node
            # we increase the size by 1 since we are just adding one
            self.size += 1


# Old Remove
    # def remove(self, key):
    #     '''
    #     Remove the value stored with the given key.

    #     Print a warning if the key is not found.

    #     Fill this in.
    #     '''
    #     pos = self._hash_mod(key)
    #     # Check if a pair exists in the bucket with matching keys
    #     if self.storage[pos] is not None and self.storage[pos].key == key:
    #         dummy_head = LinkedPair("dummy", "dummy")
    #         head = dummy_head
    #         dummy_head.next = self.storage[pos]

    #         while head.next != None:
    #             if head.next.key == key:
    #                 head.next = head.next.next
    #                 break
    #             head = head.next
    #         self.storage[pos] = dummy_head.next
    #     else:
    #         # Else print warning
    #         print("Warning: Key does not exist")


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index]:
            node = self.storage[index]
        else:
            return print("Warning: Key does not exist")
        temp = None
        while node.key != key:
            temp = node
            node = temp.next
        if node is None:
            return print("Warning: Key does not exist")
        else:
            if temp is None:
                result = node.value
                self.storage[index] = node.next
                return result
            else:
                self.size -= 1
                temp.next = node.next
                return node.value


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        '''
        pos = self._hash_mod(key)
        head = self.storage[pos]
        while head != None:
            if head.key == key:
                return head.value
            head = head.next


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        prev_storage = self.storage
        prev_capacity = self.capacity
        self.capacity = prev_capacity * 2
        self.storage = [None] * self.capacity
        for i in range(prev_capacity):
            head = prev_storage[i]
            while head != None:
                self.insert(head.key, head.value)
                head = head.next



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
