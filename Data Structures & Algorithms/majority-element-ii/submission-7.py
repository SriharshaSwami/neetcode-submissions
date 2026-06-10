class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
    # If count has less than 3 elements, no problem
            if len(count) < 3:
                continue
    # If not we gotta decrement counts of all elements and del the elements with zero count
    # We use help of a temporary hashMap i.e newCount to do that
            newCount = defaultdict(int)
            for num, c in count.items():
                if c > 1:
                    newCount[num] = c - 1
            count = newCount
            
    # Check if the elements in map are actually valid or not
        res =[]
        for num in count:
            
            if nums.count(num) > n // 3:
                res.append(num)
        return res