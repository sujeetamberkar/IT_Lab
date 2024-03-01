class PairFinder:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def find_pair(self):
        # Dictionary to store number and its index
        num_map = {}
        for i, number in enumerate(self.numbers):
            # Complement is the difference between target and the current number
            complement = self.target - number
            if complement in num_map:
                # If complement exists in map, return the current index and complement's index
                return num_map[complement], i
            num_map[number] = i
        return None  # Return None if no pair is found

# Example usage
numbers = [10, 20, 10, 40, 50, 60, 70]
target = 50
finder = PairFinder(numbers, target)
result = finder.find_pair()

if result:
    print(f"Indices: {result[0]}, {result[1]}")
else:
    print("No pair found.")
