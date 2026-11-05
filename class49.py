file = open("bucket-list.txt", "w")
file.write("1. Visit the Eiffel Tower\n")
file.write("2. Learn to play the guitar\n")
file.write("3. Code my own game\n")
file.close()
print("Bucket list saved to bucket-list.txt!")

file = open("bucket-list.txt", "r")
content = file.read()
print("Here is your bucket list:")
print(content)
file.close()

file = open("bucket-list.txt", "r")
lines = file.readlines()
print(f" You have {len(lines)} items on your bucket list.")

file.close()

file = open("bucket-list.txt", "a")
file.write("4. Go skydiving\n")
file.write("5. Write a book\n")
file.close()
print("\n 2 items added to your bucket list!")

file = open("bucket-list.txt", "r")
print("\n=== Updated Bucket List ===")
print(file.read())
file.close()