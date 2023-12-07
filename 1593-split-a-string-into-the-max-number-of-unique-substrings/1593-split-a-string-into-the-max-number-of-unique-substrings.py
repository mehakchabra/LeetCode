class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def recursive(index, cur):
            nonlocal result
            
            if index == n:
                cur_len = len(cur)

                if cur_len > result:
                    result = cur_len

            for j in range(index, n):
                tmp = s[index:j + 1]

                if tmp in cur:
                    continue

                cur[tmp] = True
                recursive(j + 1, cur)
                del cur[tmp]

        n = len(s)
        result = 0
        recursive(0, {})

        return result
                