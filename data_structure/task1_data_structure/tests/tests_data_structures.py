"""Tests for task data structures:
linked list, stack, queue, hash table, tree, graph"""

from random import randint
import pytest

from data_structure.task1_data_structures.task1_data_structures import (
    LinkedList, Queue, Stack, BinarySearchTree, HashTable, Graph)


class TestLinkedList:
    """Test linked list
    methods: append, prepend, lookup, insert, delete
    """
    @pytest.mark.parametrize("array",
                             [[randint(-50, 50) for _ in range(100)],
                              [randint(-50, 50) for _ in range(50)]],
                             [randint(-50, 50) for _ in range(100)]
                             )
    def test_prepend(self, array):
        """Test liked list prepend methods
        that add new element at first position.

        :argument  array - random gen list"""
        # create LikedList
        linked_list = LinkedList(25)

        for item in array:
            linked_list.prepend(item)
        array.append(25)
        print(linked_list, array)
        assert linked_list == array
