'''
Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''
try:
    with open("sample.txt", "r") as fh:

        data1 = fh.readline() 
        data2 = fh.readline() 
    print(f"Line 1: {data1}") 
    print(f"Line 2: {data2}")

except FileNotFoundError:
   print("Error: The File sample.txt file does not exist.")

