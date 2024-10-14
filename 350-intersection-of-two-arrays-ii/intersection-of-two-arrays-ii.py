class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        freq = {}  # Dictionary to store frequency of elements in nums1
        result = []

        # Populate the frequency map for nums1
        for num in nums1:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Iterate through nums2 and add elements to the result if present in the frequency map
        for num in nums2:
            if num in freq and freq[num] > 0:
                result.append(num)
                freq[num] -= 1  # Decrease the count to handle duplicates

        return result