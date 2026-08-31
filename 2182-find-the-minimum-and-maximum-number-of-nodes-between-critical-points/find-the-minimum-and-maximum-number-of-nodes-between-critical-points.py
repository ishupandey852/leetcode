# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # A list needs at least 3 nodes to have any critical points
        if not head or not head.next or not head.next.next:
            return [-1, -1]
            
        prev = head
        curr = head.next
        index = 1
        
        first_cp = -1
        prev_cp = -1
        min_dist = float('inf')
        
        while curr.next:
            # Check for local maxima or local minima
            is_maxima = curr.val > prev.val and curr.val > curr.next.val
            is_minima = curr.val < prev.val and curr.val < curr.next.val
            
            if is_maxima or is_minima:
                if first_cp == -1:
                    first_cp = index
                else:
                    # Update minimum distance between adjacent critical points
                    min_dist = min(min_dist, index - prev_cp)
                
                prev_cp = index
                
            prev = curr
            curr = curr.next
            index += 1
            
        # If fewer than 2 critical points were found
        if min_dist == float('inf'):
            return [-1, -1]
            
        max_dist = prev_cp - first_cp
        return [min_dist, max_dist]