# utf-8
# 2019-06-09 23:35:17

# https://leetcode.com/problems/add-two-numbers-ii/description/

# 445. Add Two Numbers II
# Medium
#
# 731
#
# 97
#
# Favorite
#
# Share
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7




class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # push into stack
        s1, s2 = [], []
        while l1 or l2:
            if l1:
                s1.append(l1.val)
                l1 = l1.next
            if l2:
                s2. append(l2.val)
                l2 = l2.next
        # pop from stack
        h = ListNode(0)
        carry = 0
        while s1 or s2:
            v1 = v2 = 0
            if s1:
                v1 = s1.pop()
            if s2:
                v2 = s2.pop()
            v = (carry + v1 + v2)%10
            carry = (carry + v1 + v2) // 10
            p = ListNode(v)
            q = h.next
            p.next = q
            h.next = p
        if carry == 1:
            h.val = 1
            return h
        return h.next


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

if __name__ == '__main__':
    s = Solution()
    l1 = [7,2,4,3]

    l2 = [5,6,4]

    l1 = [6]
    l2 = [5]

    lkl1 = make_linkedlist(l1)
    lkl2 = make_linkedlist(l2)

    res = s.addTwoNumbers(lkl1, lkl2)
    print_linkedlist(res)




