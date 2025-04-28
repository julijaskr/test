# Open the file "demofile.txt" in read mode
f = open("demofile.txt")
# Read and print the content of the file
print(f.read())
# Close the file after reading
f.close()

# Open the file "demofile.txt" in append mode
f = open("demofile.txt", "a")
# Write additional content to the file
f.write("Now the file has more content!")
# Close the file after writing
f.close()
