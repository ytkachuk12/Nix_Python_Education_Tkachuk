"""Tests for task data structures:
linked list, stack, queue, hash table, tree, graph"""

from random import randint
import pytest

from task1_data_structures import (
    LinkedList, Queue, Stack, BinarySearchTree, HashTable, Graph
)


def convert(linked_list):
    """Convert linked list object to python list
    Take each value from linked list and append it to python list

    :argument linked_list: LinkedList
    :return python list"""
    current = linked_list.head
    python_list = []
    while current:
        python_list.append(current.value)
        current = current.pointer
    return python_list


class TestLinkedList:
    """Test linked list
    methods: append, prepend, lookup, insert, delete
    """


@pytest.mark.parametrize("array",
                         [[randint(-50, 50) for _ in range(100)],
                          [randint(-50, 50) for _ in range(50)],
                         [randint(-500, 500) for _ in range(100)]]
                         )
def test_prepend(array):
    """Test liked list prepend methods
    that add new element at first position.

    :argument  array - randomly gen list"""
    # create LikedList
    prepend_linked_list = LinkedList(25)
    # add each new item on first position
    for item in reversed(array):
        prepend_linked_list.prepend(item)
    array.append(25)
    assert convert(prepend_linked_list) == array


@pytest.mark.parametrize("array",
                         [[randint(-50, 50) for _ in range(100)],
                          [randint(-50, 50) for _ in range(50)],
                         [randint(-500, 500) for _ in range(100)]]
                         )
def test_append(array):
    """Test liked list append methods
    that add new element at last position.

    :argument  array - randomly gen list"""
    # create LikedList
    append_linked_list = LinkedList(25)
    # add each new item on last position
    for item in array:
        append_linked_list.append(item)
    array.insert(0, 25)
    assert convert(append_linked_list) == array


@pytest.mark.parametrize("array",
                         [[randint(-50, 50) for _ in range(100)],
                          [randint(-50, 50) for _ in range(50)],
                         [randint(-500, 500) for _ in range(100)]]
                         )
def test_lookup(array):
    """Test liked list append find methods
    that lookup value in list
    In case value not in list no return

    :argument array - randomly gen list
    """
    # create LikedList
    find_linked_list = LinkedList(25)
    # add each new item on last position
    for item in array:
        find_linked_list.append(item)
    array.insert(0, 25)

    for item in range(100, 12):
        # take each 12 element from python list and lookup in linked list
        # index must be the same
        num = array[item]
        assert find_linked_list.lookup(num) == array.index(num)


@pytest.mark.parametrize("array",
                         [[randint(-50, 50) for _ in range(100)],
                          [randint(-50, 50) for _ in range(50)],
                         [randint(-500, 500) for _ in range(100)]]
                         )
def test_insert(array):
    """Test liked list insert methods
    that insert new element at current position.

    :argument  array - randomly gen list"""
    # create LikedList
    insert_linked_list = LinkedList(25)
    # add each new item on last position
    for item in array:
        insert_linked_list.append(item)
    array.insert(0, 25)

    # insert 20 elements in linked list and python list at special position
    for value in range(20):
        index = randint(0, 50)
        insert_linked_list.insert(index, value)
        array.insert(index, value)
    assert convert(insert_linked_list) == array


# @pytest.mark.parametrize("array",
#                          [[randint(-50, 50) for _ in range(100)],
#                           [randint(-150, 150) for _ in range(100)],
#                          [randint(-500, 500) for _ in range(100)]]
#                          )
# def test_delete(array):
#     """Test liked list delete methods
#     that delete element from list by index.
#
#     :argument  array - randomly gen list"""
#     # create LikedList
#     delete_linked_list = LinkedList(25)
#     # add each new item on last position
#     for item in array:
#         delete_linked_list.append(item)
#     array.insert(0, 25)
#
#     for _ in range(20):
#         index = randint(0, 49)
#         delete_linked_list.delete(index)
#         array.pop(index)
#     delete_linked_list.delete(0), array.pop(0)
#     assert convert(delete_linked_list) == array