class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        result = list(zip(*matrix))
        res = []
        for i in result:
            r = list(i[::-1])
            res.append(r)
        matrix[:] = res


b = [[5, 1, 9, 11],
     [2, 4, 8, 10],
     [13, 3, 6, 7],
     [15, 14, 12, 16]]
Solution().rotate(b)
print(b)