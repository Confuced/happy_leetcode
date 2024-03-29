# coding=utf-8
# 2019-06-06 13:48:23
# https://leetcode.com/problems/linked-list-cycle/description/

# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
#
#
#
# Example 1:
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
#
#
# Example 2:
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
#
#
# Example 3:
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
#
#
#
# Follow up:
#
# Can you solve it using O(1) (i.e. constant) memory?

def make_linkedlist(list1):
    a = b = ListNode(0)
    for i in list1:
        b.next = ListNode(i)
        b = b.next
    return a.next

def print_linkedlist(listNode):
    if listNode is None:
        print('linkedlist is None')
    while listNode:
        print(listNode.val, end=",")
        listNode = listNode.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        p1 = p2 = head
        while p1 and p2:
            p1 = p1.next
            if p1:
                p1 = p1.next
            else:
                return False
            p2 = p2.next
            if p1 == p2:
                return True
        return False



