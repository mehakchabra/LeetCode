class Solution:
    def countSegments(self, s: str) -> int:
        slist = list(s.split(" "))
        return (len(slist)-slist.count(""))
        
        