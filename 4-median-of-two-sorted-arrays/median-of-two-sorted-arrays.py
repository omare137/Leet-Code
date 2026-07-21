class Solution:
    
       
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        com = sorted(nums1 + nums2)
        mn = len(com)
        
        if mn % 2:
            median = com[(mn - 1) // 2]
        else:
            median = (com[(mn // 2) - 1] + com[mn // 2]) / 2
        
        return median
        


      

