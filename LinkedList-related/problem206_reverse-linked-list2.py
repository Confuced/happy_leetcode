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

    # def __repr__(self):
    #     # return self.val + 'next is ' + self.next.val if self.next else 'None'
    #     return self.val
    #
    def __str__(self):
        return self.val

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        current_node = head
        pre_node = next_node = None
        while current_node.next:
            # save the next node first
            next_node = current_node.next
            # reverse the next attribute
            current_node.next = pre_node
            # make the current node the previous node
            pre_node = current_node
            # start the next loop
            current_node = next_node
        current_node.next = pre_node
        return current_node

    def reverseList_v2(self, head: ListNode) -> ListNode:
        current_node = head
        pre_node = None
        while current_node:
            # save the next node first
            next_node = current_node.next
            # reverse the next attribute
            current_node.next = pre_node
            # make the current node the previous node
            pre_node = current_node
            # start the next loop
            current_node = next_node
        return pre_node

    # 递归法
    def reverseList_v3(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        new_head = self.reverseList_v3(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def f1(self, head):
        print('head:{},next_val:{}'.format(head.val, head.next.val if head.next else 'NONE'))
        if head is None or head.next is None:
            return head
        next = head.next
        new_head = self.f1(next)
        next.next = head
        head.next = None
        return new_head


if __name__ == '__main__':
    s = Solution()
    l1 = [1, 2, 3]
    # l1 = [1, 2]
    # l1 = [1]
    # l1 = [4, 5, 6]
    # l1 = [1, 2]
    # l1 = []
    test1 = make_linkedlist(l1)

    # l2 = []
    res = s.f1(test1)
    print_linkedlist(res)


# 下面我们来看递归解法，代码量更少，递归解法的思路是，不断的进入递归函数，直到head指向倒数第二个节点，因为head指向空或者是最后一个结点都直接返回了，newHead则指向对head的下一个结点调用递归函数返回的头结点，此时newHead指向最后一个结点，然后head的下一个结点的next指向head本身，这个相当于把head结点移动到末尾的操作，因为是回溯的操作，所以head的下一个结点总是在上一轮被移动到末尾了，但head之后的next还没有断开，所以可以顺势将head移动到末尾，再把next断开，最后返回newHead即可，代码如下：

