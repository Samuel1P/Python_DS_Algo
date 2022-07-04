from data_structures.Linked_List.Linked_List import LinkedList

class TestLinkedList:
    def setup_method(self):
        self.LL_EMPTY = LinkedList()
        self.LL = LinkedList("Ash")
        self.LL.append("Bob")
        self.LL.append("Cathy")
        self.LL.append("Dom")

    
    def test_create_linkedlist(self):
        assert isinstance(self.LL_EMPTY, LinkedList)
        assert isinstance(self.LL, LinkedList)
        
    def test_append_node(self):
        self.LL.append("Evan")
        assert self.LL.get_node(len(self.LL)-1).value == "Evan"
        self.LL_EMPTY.append("Abdul")
        assert self.LL_EMPTY.get_node(0).value == "Abdul"

    def test_prepend_node(self):
        assert self.LL.get_node(0).value == "Ash"
        self.LL.prepend("Abdul")
        assert self.LL.get_node(0).value == "Abdul"
        
    def test_pop_last_node(self):
        length_before_pop = len(self.LL)
        popped_node = self.LL.pop()
        length_after_pop = len(self.LL)
        assert popped_node.value == "Dom"
        assert length_before_pop == length_after_pop + 1

    def test_pop_first_node(self):
        length_before_pop = len(self.LL)
        popped_node = self.LL.pop_first()
        length_after_pop = len(self.LL)
        assert popped_node.value == "Ash"
        assert length_before_pop == length_after_pop + 1
    
    def test_get_node_at_index(self):
        pass
    
    # get node at index
    # insert node at index
    # set node value at index
    # remove node at index
    # reverse ll
    # https://github.com/Samuel1P/Python/blob/master/data_structures/linked_list/singly_linked_list.py
    
    def teardown_method(self):
        del self.LL