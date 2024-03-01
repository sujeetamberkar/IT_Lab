class SubsetGenerator:
    def __init__(self, nums):
        self.nums = nums
        self.result = []

    def generate_subsets(self, start=0, current=[]):
        self.result.append(current[:])
        for i in range(start, len(self.nums)):
            # Include the current number and move to the next
            current.append(self.nums[i])
            self.generate_subsets(i + 1, current)
            # Exclude the current number and backtrack
            current.pop()

    def get_subsets(self):
        self.generate_subsets()
        return self.result

nums = [4, 5, 6]
generator = SubsetGenerator(nums)
generator.get_subsets()
print(generator.result)

