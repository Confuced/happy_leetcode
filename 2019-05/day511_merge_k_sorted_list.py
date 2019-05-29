# coding=utf-8
# 23. Merge k Sorted Lists
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# 初步思路：
# 把链表拼接起来，采用冒泡排序的办法， 这种方法比较简单，容易想到。时间复杂度是 O(sum(n1,n2,n3, ...)^2)
# 第二个， 设置n个pointer, 每次扫描一遍n个pointer，时间复杂度是 o(n* sum(n1, n2, n3, n4...))
# 第三个， 两两合并，最后转成2merge的思路。

# the high-voted java solution
# https://leetcode.com/problems/merge-k-sorted-lists/discuss/10522/My-simple-java-Solution-use-recursion


# Definition for singly-linked list.
List = list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists) :
        return partion(lists, 0, len(lists)-1)


def partion(lists, l, h):
    if l == h: return lists[l]
    if l < h:
        q = int((h+l)/2)
        l1 = partion(lists, l, q)
        l2 = partion(lists, q+1, h)
        return merge(l1, l2)
    else:
        return None


def merge(l1, l2):
    if l1 is None: return l2
    if l2 is None: return l2
    if l1.val < l2.val:
        l1.next = merge(l1.next, l2)
        return l1
    else:
        l2.next = merge(l1, l2.next)
        return l2

def list_to_linked_list(listx):
    s = s1 = ListNode(0)
    for i in listx:
        s1.next = ListNode(i)
        s1 = s1.next
    return s.next


if __name__ == '__main__':
    list1 = [1, 4, 5]
    list2 = [2, 3, 4]
    list3 = [2, 6]
    link_list1 = list_to_linked_list(list1)
    link_list2 = list_to_linked_list(list2)
    link_list3 = list_to_linked_list(list3)

    s = Solution()
    l1 = s.mergeKLists([link_list1, link_list2, link_list3])
    while l1:
        print(l1.val)
        l1 = l1.next
