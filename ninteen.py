# Write a Python class to find validity of a string of parentheses, '(',
# ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid



class check_valid:
   def checking_validity(self, check_string):
        li, di = [], {"(": ")", "{": "}", "[": "]"}
        for i in check_string:
            if i in di:
                li.append(i)
            elif len(li) == 0 or di[li.pop()] != i:
                return False
        return len(li) == 0

print(check_valid().checking_validity("(){}[]"))
print(check_valid().checking_validity("()[{)}"))