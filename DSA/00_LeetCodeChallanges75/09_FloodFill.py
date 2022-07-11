'''
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

https://leetcode.com/problems/flood-fill/
'''

class Solution:
    def floodFillDFS(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        height = len(image)
        width = len(image[0])
        src_color = image[sr][sc]

        def dfs(x, y):
            if x < 0 or x >= width or y < 0 or y >= height or image[x][y] == newColor or image[x][y] != src_color:
                return
            
            image[x][y] = newColor

            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y +1)
            dfs(x, y -1)

        dfs(sr, sc)

        return image

    def floodFillBFS(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        queue = []
        queue.append([sr,sc])
        width, height = len(image[0]), len(image)
        source_color = image[sr][sc]

        while queue:
            curr_row, curr_col = queue.pop(0)

            if curr_row < 0 or curr_col < 0 or curr_row >= height or curr_col >= width or image[curr_row][curr_col] == newColor or image[curr_row][curr_col] != source_color:
                continue

            image[curr_row][curr_col] = newColor

            queue.append([curr_row-1, curr_col])
            queue.append([curr_row+1, curr_col])
            queue.append([curr_row, curr_col-1])
            queue.append([curr_row, curr_col+1])

        return image

