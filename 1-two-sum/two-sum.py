class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        n=nums
        sortedNums=sorted(n)
        while left<right:
            cur = sortedNums[left] + sortedNums[right]
            if cur == target:
                break
            elif cur<target:
                left +=1
            else:
                right-=1
    
        left=n.index(sortedNums[left])
        n[left]=1.1
        right=n.index(sortedNums[right])
        return (left, right)

        



        