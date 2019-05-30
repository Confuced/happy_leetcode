list1 = []

def test1(list_1):
    list_1.pop()

def test2(list_1):
    list_1.append(3)

if __name__ == '__main__':
    test2(list1)
    test2(list1)
    print(list1)