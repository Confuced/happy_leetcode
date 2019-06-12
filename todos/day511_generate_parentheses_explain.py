# coding=utf-8

# source:
# https://leetcode.com/problems/generate-parentheses/discuss/10100/Easy-to-understand-Java-backtracking-solution

params_all = []

def generateParenthesis(n):
    list1 = [] # 接受每个正确结果的容器
    backtrack(list1, '', 0, 0, n)
    return list1

def backtrack(list1, str1, open, close, max):
    if list1 == [] and str1 == '(())':
        pass
    params = 'list1:{}, str1: {}, open: {}, close: {}, max:{}'.format(list1, str1, open, close, max)
    params_all.append(params)
    # 当前结果如果长度刚好OK，那么说明OK了，可以结束了， 递归出口。
    if len(str1) == max*2:
        list1.append(str1)
        return

    if open < max: # 如果打开的小于总的， 继续增加打开的。
        backtrack(list1, str1+'(', open+1, close, max)
    if close < open: # 如果闭合的括号小于打开的， 让他闭合。
        backtrack(list1, str1+')', open, close+1, max)


if __name__ == '__main__':
    # print(generateParenthesis(1))
    print(generateParenthesis(3))

    # 这段代码可以带引每次递归时传入的参数
    # if params_all:
    #     with open('params_all.txt', 'a+') as f:
    #         for i in params_all:
    #             f.write('{}\n'.format(i))

    # list1:[], str1: , open: 0, close: 0, max:2
    # list1:[], str1: (, open: 1, close: 0, max:2
    # list1:[], str1: ((, open: 2, close: 0, max:2
    # list1:[], str1: ((), open: 2, close: 1, max:2
    # list1:[], str1: (()), open: 2, close: 2, max:2
    # list1:['(())'], str1: (), open: 1, close: 1, max:2
    # list1:['(())'], str1: ()(, open: 2, close: 1, max:2
    # list1:['(())'], str1: ()(), open: 2, close: 2, max:2

    # list1:[], str1: , open: 0, close: 0, max:3
    # list1:[], str1: (, open: 1, close: 0, max:3
    # list1:[], str1: ((, open: 2, close: 0, max:3
    # list1:[], str1: (((, open: 3, close: 0, max:3
    # list1:[], str1: (((), open: 3, close: 1, max:3
    # list1:[], str1: ((()), open: 3, close: 2, max:3
    # list1:[], str1: ((())), open: 3, close: 3, max:3
    # list1:['((()))'], str1: ((), open: 2, close: 1, max:3
    # list1:['((()))'], str1: (()(, open: 3, close: 1, max:3
    # list1:['((()))'], str1: (()(), open: 3, close: 2, max:3
    # list1:['((()))'], str1: (()()), open: 3, close: 3, max:3
    # list1:['((()))', '(()())'], str1: (()), open: 2, close: 2, max:3
    # list1:['((()))', '(()())'], str1: (())(, open: 3, close: 2, max:3
    # list1:['((()))', '(()())'], str1: (())(), open: 3, close: 3, max:3
    # list1:['((()))', '(()())', '(())()'], str1: (), open: 1, close: 1, max:3
    # list1:['((()))', '(()())', '(())()'], str1: ()(, open: 2, close: 1, max:3
    # list1:['((()))', '(()())', '(())()'], str1: ()((, open: 3, close: 1, max:3
    # list1:['((()))', '(()())', '(())()'], str1: ()((), open: 3, close: 2, max:3
    # list1:['((()))', '(()())', '(())()'], str1: ()(()), open: 3, close: 3, max:3
    # list1:['((()))', '(()())', '(())()', '()(())'], str1: ()(), open: 2, close: 2, max:3
    # list1:['((()))', '(()())', '(())()', '()(())'], str1: ()()(, open: 3, close: 2, max:3
    # list1:['((()))', '(()())', '(())()', '()(())'], str1: ()()(), open: 3, close: 3, max:3



    # print(generateParenthesis(3))