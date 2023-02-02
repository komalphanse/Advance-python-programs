f=open("file2.txt","r")
content=f.readline()
content1=f.readlines()#it returns the list of the lines till end of file is reached
print(content)
print(content1)
f.close()#close the file 