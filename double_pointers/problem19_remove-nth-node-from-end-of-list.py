# coding=utf-8
# 5月6日
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# 解法讲解：
#     https://github.com/MisterBooo/LeetCodeAnimation/blob/master/notes/LeetCode%E7%AC%AC19%E5%8F%B7%E9%97%AE%E9%A2%98%EF%BC%9A%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E5%80%92%E6%95%B0%E7%AC%ACN%E4%B8%AA%E8%8A%82%E7%82%B9.md
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        p, q = head, head
        for i in range(0, n):
            q = q.next

        # 这段代码的意义是什么呢？
        # 解释一下： 如果q往前走了n步，变成了None，那说明什么? 说明n=链表的长度。
        # 说明要删除第一个元素，所以此时把head往后移动一下并直接返回
        if not q:
            return head.next

        # 我这里解释一下下面这句代码为什么是 q.next 而不是q呢?
        # 原因如下： 假如到了最后一个结点，如果是检查q.next是否为空，那么就到此停下来了
        #                              如果是检查q是否为空，那么q还会往前再走一步，q退出循环的时候会变成空值，而p则会往前多走一步
        # 不理解的同学可以自己测试一下。
        # 在这里我也是花了好长的时间去琢磨和理解为什么这么写。这里非常关键
        while q.next:
            p = p.next
            q = q.next

        p.next = p.next.next
        return head


if __name__ == '__main__':
    l1 = ListNode(1)

    l2 = l1
    for i in range(2, 6):
        l2.next = ListNode(i)
        l2 = l2.next

    s = Solution()
    l2 = s.removeNthFromEnd(l1, 2)

    while l2:
        print(l2.val)
        l2 = l2.next
