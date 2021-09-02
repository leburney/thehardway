from sys import argv
# getting input from the command line
# unpack/assigning variables
script, filename = argv
# opens a file
txt = open(filename)
# print the filename and the content
print(f"Here's your file {filename}:")
print(txt.read())
# opening a file using input
print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())