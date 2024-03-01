class PowerCalculator:
    def pow(self, x, n):
        # Base case
        if n == 0:
            return 1
        # Negative powers
        elif n < 0:
            x = 1 / x
            n = -n
        return self.fast_pow(x, n)

    def fast_pow(self, x, n):
        # Base case
        if n == 0:
            return 1
        # Recursive step
        half = self.fast_pow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

# Example usage
calculator = PowerCalculator()
x = 2
n = 10
print(f"{x} to the power of {n} is: {calculator.pow(x, n)}")

x = 2
n = -2
print(f"{x} to the power of {n} is: {calculator.pow(x, n)}")
