
try:
    file = open("sample.txt", "r")
    content = file.read()
    print("File Content:\n", content)
    file.close()

except FileNotFoundError:
    print("Error: File does not exist.")

finally:
    print("Program execution completed.")