"""判断字符串是否属于另一个大字符串，
判断字符串的长度是否为1
且判断字符串否为关键字 用keyword库里面的kwlist方法"""

import keyword
import string
import sys

StarsWith = string.ascii_letters + '_'   #首字母符合的条件
OtherSymbol =string.ascii_letters + '_' + string.digits #非首字母
def Check(s):
    if s[0] in StarsWith:
        if len(s) == 1:
            print("length 1 is value",end=",a")
            if s in keyword.kwlist:
                print("s is a keyword")
            else:
                print("but not a keyword")
        else:
            for j in s[1:]:
                if j not in OtherSymbol:
                    print("is not a value")
                    sys.exit()
            if s in keyword.kwlist:
                print("s is a keyword")
    else:
        print("s not a value")

if __name__ == '__main__':
    s = input("input a string:")
    Check(s)