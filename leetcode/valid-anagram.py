'''LeetCode
Valid Anagram
https://leetcode.com/problems/valid-anagram/
'''

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)

        # not required, but an easy way to skip unnecessary computation
        if( len(s) != len(t)):
            return False
        
        for character in s:
            d[character] += 1
        
        for character in t:
            d[character] -= 1
        
        if any(d.values()):
            return False
        
        return True

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    solution = Solution()
    print(solution.isAnagram(s, t))