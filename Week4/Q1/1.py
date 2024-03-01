class Sol:
    def __init__(self, nums):
        self.nums = nums
        self.result = []

    def helper(self, partial_answer, index):
        if index == len(self.nums):
            self.result.append(partial_answer.copy())
            return

        # Without current number
        self.helper(partial_answer, index + 1)
        
        # With current number
        partial_answer.append(self.nums[index])
        self.helper(partial_answer, index + 1)
        partial_answer.pop()  # Remove the last element added for backtracking

    def get_subsets(self):
        self.helper([], 0)

# Initialize the Sol class with a list of numbers
nums = [4, 5, 6]
generator = Sol(nums)
generator.get_subsets()
print(generator.result)
