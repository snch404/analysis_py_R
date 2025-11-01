def count_letters(s):
    d={}
    for char in s:
        if char==" ":
            continue
        if char not in d.keys():
            d[char]=1
        else:
            d[char]+=1
    return d
s=input("Enter a string:")
dic=count_letters(s)
for j in dic:
    print(j,":",dic[j])