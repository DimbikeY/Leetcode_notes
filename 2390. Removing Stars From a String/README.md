# You are given a string s, which contains stars *.  

# In one operation, you can:  

## Choose a star in s.  
## Remove the closest non-star character to its left, as well as remove the star itself.  
## Return the string after all stars have been removed.  

### Note:  

### The input will be generated such that the operation is always possible.  
### It can be shown that the resulting string will always be unique.  
# Intuition  
<!-- Describe your first thoughts on how to solve this problem. -->  

# Approach  
<!-- Describe your approach to solving the problem. -->  

# Complexity  
- Time complexity:  
<!-- Add your time complexity here, e.g. $$O(n)$$ -->  

- Space complexity:  
<!-- Add your space complexity here, e.g. $$O(n)$$ -->  

# Code  
```  
class Solution:  
    def removeStars(self, s: str) -> str:  
        while '*' in s:  
            number = s.find('*')  
            s = s[:number-1] + s[number+1:]  
        return s  
```  
