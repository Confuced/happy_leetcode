# coding=utf-8
# 2019-06-06 13:48:23
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# Example 1:
#
# Input: 1->1->2
# Output: 1->2
# Example 2:
#
# Input: 1->1->2->3->3
# Output: 1->2->3

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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.next.val == head.val else head


# 代码解释：
# if not head or not head.next: return head
# 如果head为空，也就是说head本身为空，这个链表为空，直接返回
# 或者是链表的最后一个元素， 那就返回最后一个元素
# 这第一句话是表明 递归的出口

# head.next = self.deleteDuplicates(head.next)
# 然后，我们开始进入递归， 修改当前结点的下一个结点，下一个结点到底是啥？我们看下一句话

if __name__ == '__main__':
    s = Solution()
    # l1 = [1, 1, 2, 3]
    # l1 = [1, 2]
    # l1 = [1]
    # l1 = [4, 5, 6]
    # l1 = [1, 2]
    l1 = []
    test1 = make_linkedlist(l1)

    # l2 = []
    res = s.deleteDuplicates(test1)
    print_linkedlist(res)
