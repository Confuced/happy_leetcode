# coding=utf-8
# https://leetcode.com/problems/# /description/

# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# reference:

# Definition for singly-linked list.

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

class Solution:
    new_head = None

    def reverseList(self, head: ListNode) -> ListNode:
        self.reverse(head, None)
        return self.new_head

    def reverse(self, head, pre):
        if head is None:
            self.new_head = pre
            return
        self.reverse(head.next, head)
        head.next = pre

    def reverse_v2(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self.reverse_v2(n, node)





if __name__ == '__main__':
    s = Solution()
    # l1 = [1, 2, 3, 4]
    l1 = [1, 2, 3]
    # l1 = [1, 2]
    # l1 = [1]
    # l1 = []
    test1 = make_linkedlist(l1)

    # l2 = []
    res = s.reverseList(test1)
    print_linkedlist(res)


