# coding=utf-8

def fabonacci(n):
    if n ==1 or n == 2:
        return 1
    return fabonacci(n-1)+fabonacci(n-2)

# 1, 1, 2, 3, 5, 8

if __name__ == '__main__':
    print(fabonacci(6))