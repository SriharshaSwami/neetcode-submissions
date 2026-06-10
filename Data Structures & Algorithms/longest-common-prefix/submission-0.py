class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if not strs:
            return prefix
        prefix = strs[0]
        for string in strs:
            while prefix and not string.startswith(prefix):
                prefix = prefix[:-1]
        return prefix 
