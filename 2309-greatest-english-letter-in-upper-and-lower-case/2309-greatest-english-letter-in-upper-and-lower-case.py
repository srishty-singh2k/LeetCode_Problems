class Solution:
    def greatestLetter(self, s: str) -> str:
        common = ""
        for each in s:
            if each.isupper() and each.lower() in s:
                if each > common:
                    common = each
        return common
        
            