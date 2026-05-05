class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m  = len(nums1)
        n = len(nums2)

        if n>m: 
            return self.findMedianSortedArrays(nums2,nums1)
        
        final = []
        x = 0 
        y = 0

        while x < m and y < n: 
            if nums1[x] < nums2[y]:
                final.append(nums1[x])
                x += 1
            else: 
                final.append(nums2[y])
                y += 1 
        
        if x < m: 
            for i in range(x,m):
                final.append(nums1[i])
        
        if y < n: 
            for i in range(y,n):
                final.append(nums2[i])

        l = len(final)

        if l % 2 == 1:
            return float(final[l//2])
        else: 
            mid = l//2
            return (final[mid-1] + final[mid]) /2.0

        



        
        
        