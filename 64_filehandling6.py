#open the file.txt in read cause error if no such file exists

f=open("file2.txt","r")
content=f.read(10)
print(type(content))
print(content)
f.close()