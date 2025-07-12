class ParathesesMatch:
   def match_pattern(self, s)-> bool:
      stack=[]
      for para in s:
         if para =='[':
            stack.append(']')
         elif para == '{':
            stack.append('}')
         elif para == '(':
            stack.append(')')
         elif not stack or para!= stack.pop():
            return False
      return not stack
   
if __name__=='__main__':
   pm = ParathesesMatch()
   print(pm.match_pattern("()"))  # True
   print(pm.match_pattern("()[]{}"))  # True
   print(pm.match_pattern("(]"))  # False
   print(pm.match_pattern("([)]"))  # False
   print(pm.match_pattern("{[]}"))  # True
    