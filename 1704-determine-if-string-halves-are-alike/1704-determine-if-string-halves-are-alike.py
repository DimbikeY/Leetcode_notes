class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels =  set("aeiouAEIOU")
        i, j = 0, len(s) - 1
        a, b = 0, 0
        while i < j:
            if s[i] in vowels:
                a += 1
            if s[j] in vowels:
                b += 1
            i += 1
            j -= 1
        return a == b
