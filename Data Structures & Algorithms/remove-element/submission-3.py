class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        TWO-POINTER SOLUTION:
        - write pointer:  tracks position where next valid element 
        should be placed and counts number of valid elements
        - read pointer:  iterates through original array, checking 
        each element to determine whether it should be kept
        '''
        write = 0                               
        for read in range(len(nums)):           
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        return write