class Palindrome:    
    def getLongestPalindrome(self,A,n):
      s_list = [s for s in A]
      A = '#' + '#'.join(s_list) + '#'
      max_length = 0
      length = len(A)
      for index in range(0, length):
        r_length = self.get_length(A, index)
        if max_length < r_length:
          max_length = r_length
      return max_length
    
    def get_length(self,A, index):
      # 循环求出index为中心的最长回文字串
      length = 0
      r_ = len(A)
      for i in range(1,index+1):
        if index+i < r_ and A[index-i] == A[index+i]:
          length += 1
        else:
          break
      return length