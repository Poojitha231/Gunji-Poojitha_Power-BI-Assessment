#Creating a new file and next write
with open("sample.txt", "w") as file:
    file.write("HI!\n")

#Append new content
with open("sample.txt", "a") as file:
    file.write("HELLO AGAIN!\n")

#Read the content in the file
with open("sample.txt", "r") as file:    
    content = file.read()

print("File content from the beginning:")
print(content)