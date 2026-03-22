"""
Test Suite for Build_Tree_From_List utility
"""
from data_structures.Trees.Build_Tree_From_List import build_tree, tree_to_list


class TestBuildTree:
    """
    Test Class
    """
    def test_one_standard_tree(self):
        """
                3
               / \
              9   20
                 / \
                15   7
        """
        values = [3, 9, 20, None, None, 15, 7]
        root = build_tree(values)
        assert root.val == 3
        assert root.left.val == 9
        assert root.right.val == 20
        assert root.left.left is None
        assert root.left.right is None
        assert root.right.left.val == 15
        assert root.right.right.val == 7

    def test_two_single_node(self):
        root = build_tree([1])
        assert root.val == 1
        assert root.left is None
        assert root.right is None

    def test_three_empty_input(self):
        root = build_tree([])
        assert root is None

    def test_four_none_root(self):
        root = build_tree([None])
        assert root is None

    def test_five_left_skewed(self):
        """
            1
           /
          2
         /
        3
        """
        values = [1, 2, None, 3]
        root = build_tree(values)
        assert root.val == 1
        assert root.left.val == 2
        assert root.right is None
        assert root.left.left.val == 3

    def test_six_right_skewed(self):
        # 1 -> right -> 2 -> right -> 3
        values = [1, None, 2, None, 3]
        root = build_tree(values)
        assert root.val == 1
        assert root.left is None
        assert root.right.val == 2
        assert root.right.right.val == 3

    def test_seven_full_tree(self):
        # complete tree: 1 with children 2,3 each having children 4,5 and 6,7
        values = [1, 2, 3, 4, 5, 6, 7]
        root = build_tree(values)
        assert root.val == 1
        assert root.left.val == 2
        assert root.right.val == 3
        assert root.left.left.val == 4
        assert root.left.right.val == 5
        assert root.right.left.val == 6
        assert root.right.right.val == 7


class TestTreeToList:
    """
    Test Class
    """
    def test_one_roundtrip(self):
        values = [3, 9, 20, None, None, 15, 7]
        root = build_tree(values)
        actual = tree_to_list(root)
        assert actual == values

    def test_two_single_node(self):
        root = build_tree([1])
        actual = tree_to_list(root)
        assert actual == [1]

    def test_three_empty_tree(self):
        actual = tree_to_list(None)
        assert actual == []

    def test_four_left_skewed_roundtrip(self):
        values = [1, 2, None, 3]
        root = build_tree(values)
        actual = tree_to_list(root)
        assert actual == values

    def test_five_full_tree_roundtrip(self):
        values = [1, 2, 3, 4, 5, 6, 7]
        root = build_tree(values)
        actual = tree_to_list(root)
        assert actual == values
