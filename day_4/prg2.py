#Now take source file name and destination file name from the user. 
#Use exception handling to report "FileNotFoundError", if any, for the source file. 
#Copy the source text file to the destination.
import os.path
try:
    sfn = input("Enter source file name: ")
    ifile= open(sfn, 'r')
except FileNotFoundError:
    print("The file", sfn, "does not exist.")
else:
    dfn = input("Enter destination file name: ")
    ofile = open(dfn, 'w')
    for line in ifile:
        ofile.write(line)
    ifile.close()
    ofile.close()
    print("File copied successfully from", sfn, "to", dfn)
    
