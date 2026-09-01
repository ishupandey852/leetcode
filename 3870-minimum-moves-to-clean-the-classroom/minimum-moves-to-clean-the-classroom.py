from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start_r = start_c = -1
        litter_coords = []
        
        # 1. Identify start position and assign bit index to each litter cell
        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]
                if cell == 'S':
                    start_r, start_c = r, c
                elif cell == 'L':
                    litter_coords.append((r, c))
                    
        total_litters = len(litter_coords)
        if total_litters == 0:
            return 0
            
        litter_map = {pos: i for i, pos in enumerate(litter_coords)}
        target_mask = (1 << total_litters) - 1
        
        # 2. BFS Initialization
        # Queue stores tuples: (r, c, mask, cur_energy, moves)
        queue = deque([(start_r, start_c, 0, energy, 0)])
        
        # best_energy[r][c][mask] stores the max remaining energy for that state
        best_energy = {}
        best_energy[(start_r, start_c, 0)] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, mask, cur_e, moves = queue.popleft()
            
            # Check if current state has already been surpassed by a better path
            if best_energy.get((r, c, mask), -1) > cur_e:
                continue
                
            # Try moving in all 4 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Out of bounds or obstacle check
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_e = cur_e - 1
                    
                    if next_e < 0:
                        continue  # Cannot move if out of energy
                        
                    next_cell = classroom[nr][nc]
                    next_mask = mask
                    
                    # Reset energy if on 'R'
                    if next_cell == 'R':
                        next_e = energy
                    # Collect litter if on 'L'
                    elif next_cell == 'L':
                        if (nr, nc) in litter_map:
                            next_mask |= (1 << litter_map[(nr, nc)])
                            
                    # Success condition: All litter items collected
                    if next_mask == target_mask:
                        return moves + 1
                        
                    # Pruning: Only proceed if this reach achieves higher remaining energy
                    if next_e > best_energy.get((nr, nc, next_mask), -1):
                        best_energy[(nr, nc, next_mask)] = next_e
                        queue.append((nr, nc, next_mask, next_e, moves + 1))
                        
        return -1