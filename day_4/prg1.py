import os.path
file=input("Enter the file name: ")
if os.path.isfile(file):
    f=open(file, "r")
    cc=0
    cl=0
    for line in f:
        cc+=len(line)
        cl+=1
    f.close()
    print(cc,"characters &",cl,"lines")
else:
    print("File does not exist")
