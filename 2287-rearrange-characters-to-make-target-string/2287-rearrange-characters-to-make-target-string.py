class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        maxx = []
        for i in range(len(set(target))):
            t_count = target.count(target[i]) # count the no of occurrence of letter in target string
            s_count = s.count(target[i]) # count the no of occurrence of target letter in s
            if t_count <= s_count:
                maxx.append(s_count // t_count)
            else:
                return 0
        return min(maxx)
        