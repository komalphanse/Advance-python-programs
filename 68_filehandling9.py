f= open("file2.txt","r") 
print("the file pointer is at byte:",f.tell())
content=f.read()
print("after reading the filepointer is at:",f.tell())
f.close()    