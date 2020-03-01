# write the data in a file
file1 = open("myfile.txt", "w")
file1.write("Hello World\n")
file1.writelines("This FYCS\nWelcome to python programming\nhello world i am vector\n so sad i am sad nooo \n")
file1.close()

file1 = open("myfile.txt", "r+")

print("output of read function is ")
print(file1.read())

file1.seek(0)
print("output of read function is ")
print(file1.readline())

file1.seek(0)
print("output of read function is ")
print(file1.readlines())

file1.seek(0)
print("output of read function is ")
print(file1.read(5))

file1.seek(0)
print("output of readline(9) function is ")
print(file1.readline(9))

file1.seek(0)
print("output of readlines function is ")
print(file1.readlines())
file1.close()
