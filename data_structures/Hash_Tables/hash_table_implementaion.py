"""
Hash Table implementation using a list
"""

class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size
    
    def print_table(self):
        for i in range(len(self.data_map)):
            print(f"{i}: {self.data_map[i]}")
    
    def __hash(self, key):
        hash = 0
        for char in  key:
            hash = (hash + ord(char)) % (len(self.data_map))
        return hash
    
    def set_item(self, key, value):
        index = self.__hash(str(key))
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        return True
    
    def get_item(self, key):
        index = self.__hash(str(key))
        if self.data_map[index] is not None:
            for key_value in self.data_map[index]:
                if key == key_value[0]:
                    return key_value
        return None
    
    """
    # TO DO
    def remove_item
    def update_value
    """
    
    def keys(self):
        all_keys = []
        for item_list in self.data_map:
            if item_list is not None:
                for item in item_list:
                    all_keys.append(item[0])
        return all_keys
        
ht = HashTable()
print("-"*50)
ht.print_table()
print("-"*50)
#print(ht.__hash("AMA"))
#print(ht._hash("MAA"))
ht.set_item("two", 2)
ht.set_item("three", 3)
ht.set_item("owt", 22)
print("-"*50)
ht.print_table()
print("-"*50)
# print(ht.get_item("two"))
# print(ht.get_item("three"))
# print(ht.get_item("two"))
print(ht.keys())