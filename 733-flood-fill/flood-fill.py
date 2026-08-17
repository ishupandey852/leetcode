class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        
        # If the starting pixel is already the target color, no fill needed
        if start_color == color:
            return image
            
        m, n = len(image), len(image[0])
        
        def dfs(r, c):
            # Check bounds and matching initial color
            if 0 <= r < m and 0 <= c < n and image[r][c] == start_color:
                image[r][c] = color
                # Explore 4 directions
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
                
        dfs(sr, sc)
        return image