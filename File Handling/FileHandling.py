# file=open("text.txt",'r')
# content=file.readline()
# content=file.readline()
# content=file.readline()
# content=file.readline()
# print(content)
# file.close()

# file=open("text.txt",'w')
# file.write("I don't smoke!\nI don't drink!")
# file.close()

# file=open("text.txt",'a')
# file.write("\nI don't smoke!\nI don't drink!")
# file.close()

file1=open("text.txt",'r')
existing_content=file1.read()
file1.close()

file2=open("text.txt",'w')
file2.write("I don't smoke!\nI don't drink!\n"+existing_content)
file2.close()