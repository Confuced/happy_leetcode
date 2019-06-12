# coding=utf-8
#  question: 给了ABCDE 这5个字母，求5个字母的全排列，不许重复使用字母。


def full_arrangement(alphabets: str) -> list:
    """
    :param alphabets: 字母列表
    :return:
    """
    results = []
    arrange(alphabets, '', results)
    return results


def arrange(alphabets, result, results):
    if len(alphabets) == 1:
        results.append(result + alphabets[0])
        return

    for i in range(0, len(alphabets)):
        arrange(alphabets[0:i]+alphabets[i+1:], result+alphabets[i], results)


if __name__ == '__main__':
    print(full_arrangement('ABC'))