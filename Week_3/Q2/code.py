# input_file=input("Enter a Orignal File")
# output_file= input("Enter the reserved file name")
try:
    with open("a.txt", 'r') as file:
        content = file.read()
    reversed_content = content[::-1]
    with open("b.txt", 'w+') as file:
        file.write(reversed_content)
    print("File content reversed successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
