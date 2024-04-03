class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        self.patternString = {}
        res = self.backtrack(pattern, s, 0, 0)

        for k, v in self.patternString.items():
            self.patternString[k] = ""
            if v in self.patternString.values(): return False

        return res
    
    def backtrack(self, pattern, s, j, index):
        if j == len(pattern) and index == len(s): return True
        elif j >= len(pattern) or index >= len(s): return False
        
        for i in range(index, len(s)):
            curr = s[index: i + 1]
            if pattern[j] in self.patternString and len(curr) == len(self.patternString[pattern[j]]) and self.patternString[pattern[j]] != curr: return False

            if pattern[j] not in self.patternString: self.patternString[pattern[j]] = curr
            elif pattern[j] in self.patternString and len(curr) < len(self.patternString[pattern[j]]): continue
            if pattern[j] in self.patternString and self.patternString[pattern[j]] == curr and self.backtrack(pattern, s, j + 1, i + 1): return True
            if pattern[j] in self.patternString: self.patternString.pop(pattern[j])
        return False
