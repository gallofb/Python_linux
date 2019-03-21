# class str:
#     def list(self,number):
#         list = [str(i) for i in number]
#         print(list)
#         if len(list) == 0:
#             return
#         if len(list) == 1:
#             return int(list[0])
#         result = ""
#         for i in range(len(list)-1):
#             if result > list[i+1]:
#                 result = list[i]+result
#             else:
#                 result = result + list[i]
#         return int(result)
#
#
# if __name__ == '__main__':
#     bs = str()
#     list = [5,1,8,3,45,12,1]
#     print(bs.list(list))
#
class s:
    def number(self,number):
        list = [str(i) for i in number]
        if len(list) == 0:
            return
        if len(list) == 1:
            return int(list[0])
        result = ""
        for i in range(len(list)):
            if result > list[i]:
                    result = list[i]+result
            else:
                    result = result + list[i]
        return int(result)
#
st = s()
number = [1,2,3,4,5]
print(st.number(number)
)