"""给出一个字符串统计字符串中出现次数最多的字母"""
def most_number(str):
    if str is None:
        return
    The_key = list(set(list(str)))
    print(The_key)
    The_dct = {}.fromkeys(The_key,0)
    print(The_dct)
    for i in list(str):
        The_dct[i] += 1
    print()
    for key in The_dct.keys():
        if The_dct[key] == max(The_dct.values()):
            print("key = %s,values = %s" %(key,The_dct[key]))

    print(The_dct)
if __name__ == '__main__':
    str = "abcd"
    most_number(str)


