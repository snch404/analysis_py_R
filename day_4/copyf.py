import os.path
import sys

f1=input("Enter a source file: ").strip()
f2=input("Enter target file: ").strip()

if os.path.isfile(f2):
    print(f2+" does not exist")
    sys.exit()
infile=open(f1,"r")
outfile=open(f2,"w")

cl=cc=0
for line in infile:
    cl+=1
    cc+=len(line)
    outfile.write(line)
print(cl,"lines and",cc,"chars copied")
infile.close()
outfile.close()