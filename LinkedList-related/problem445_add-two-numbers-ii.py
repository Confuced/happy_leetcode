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


head = ListNode(0)


def f1(l1, l2):
    if not l1:
        return 0
    c = f1(l1.next, l2.next)
    carry = (l1.val + l2.val + c) // 10
    val = (l1.val + l2.val + c) - carry * 10
    p = head.next
    q = ListNode(val)
    head.next = q
    q.next = p
    return carry



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1h = l1
        l2h = l2
        n = 0
        while l1 and l2:
            l1 = l1.next
            l2 = l2.next
        if l2:
            l1, l2 = l2, l1
        while l1:
            l1 = l1.next
            n += 1
        l2h_new = l2hr = ListNode(0)
        for i in range(0, n-1):
            l2hr.next = ListNode(0)
            l2hr = l2hr.next
        l2hr.next = l2h

        c = f1(l1h, l2h_new)
        if c == 1:
            p = head.next
            q = ListNode(c)
            head.next = q
            q.next = p
        return head.next




if __name__ == '__main__':
    s = Solution()
    l1 = [1,2,3]
    l2 = [1,8]
    l2 = []

    lkl1 = make_linkedlist(l1)
    lkl2 = make_linkedlist(l2)

    # l2 = []
    res = s.addTwoNumbers(lkl1, lkl2)
    print_linkedlist(res)


