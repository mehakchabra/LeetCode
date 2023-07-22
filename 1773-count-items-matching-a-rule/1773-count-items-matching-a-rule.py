class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for i in range(0, len(items)):
            if ruleKey == "type":
                if items[i][0] == ruleValue:
                    count += 1
            elif ruleKey == "color":
                if items[i][1] == ruleValue:
                    count += 1
            elif ruleKey == "name":
                if items[i][2] == ruleValue:
                    count += 1
        return count