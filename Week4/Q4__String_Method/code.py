class StringPrinter:
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Enter a string: ")

    def print_String(self):
        print(self.str1.upper())

# Example usage
sp = StringPrinter()
sp.get_String()  # This will prompt the user to enter a string
sp.print_String()  # This will print the entered string in upper case
