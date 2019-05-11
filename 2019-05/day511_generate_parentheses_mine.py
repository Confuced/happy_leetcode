# coding=utf-8
# problem 22: 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

def generate_parentheses(n):
    results = []
    result = ''
    generate_one(results, result, n, 0, 0)
    return results

def generate_one(results, result, n, lefts, rights):
    if len(result) == 2*n:
        results.append(result)
        return

    if lefts < n:
        generate_one(results, result+'(', n, lefts+1, rights)
    if rights < lefts:
        generate_one(results, result + ')', n, lefts, rights+1)


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        results = []
        result = ''
        self.generate_one(results, result, n, 0, 0)
        return results

    def generate_one(self,results, result, n, lefts, rights):
        if len(result) == 2 * n:
            results.append(result)
            return

        if lefts < n:
            self.generate_one(results, result + '(', n, lefts + 1, rights)
        if rights < lefts:
            self.generate_one(results, result + ')', n, lefts, rights + 1)

if __name__ == '__main__':
    print(generate_parentheses(3))

