# 733. Flood Fill (Easy)
# Given an image represented as a grid of integers, a starting pixel (sr, sc), and a new
# color, flood fill the image starting at that pixel, replacing all connected pixels
# (4-directionally) of the original color with the new color.
# Approach: DFS from the start pixel, recoloring matching connected pixels and recursing
# to neighbors, guarding against infinite recursion when the new color equals the old
# color. Time O(rows*cols), space O(rows*cols) worst case recursion.

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if old_color == color:
            return image

        rows, cols = len(image), len(image[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != old_color:
                return
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image


if __name__ == "__main__":
    image1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    expected1 = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert Solution().floodFill(image1, 1, 1, 2) == expected1

    image2 = [[0, 0, 0], [0, 0, 0]]
    expected2 = [[2, 2, 2], [2, 2, 2]]
    assert Solution().floodFill(image2, 0, 0, 2) == expected2
    print("All tests passed.")
