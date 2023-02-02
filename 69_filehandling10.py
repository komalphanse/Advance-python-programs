f=open("file2.txt","r")
print("th file pointer is at byte",f.tell())
f.seek(10)
print("after reading the filepointer is at:",f.tell())