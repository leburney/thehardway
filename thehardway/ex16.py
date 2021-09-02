from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit ctrl -C")
print("If you do want this, hit RETURN.")

input("?")

print("Opening the file")
target = open(filename, 'w')
# w 'opens' the file in a state to be written to and
# truncates any existing data in the file
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file:")

target.write(f"{line1}\n{line2}\n{line3}")


print("And finally, we close it.")
target.close()

# study drill (2)
# txt = open(filename)
# print(txt.read())
# txt.close()



