#Simple file operation in python......
f=open("pract.txt",'r')# syntax: open("file_name",'mode')mode=r,w,a r=read,w=write,a=append, x=
data=f.read()
print(data)

data1=f.readlines()
print(data1)

data2=f.readline()
print(data2)

data3=f.readline()
print(data3)

f.close()
"""
#write opetarion...with new to create file and wite in it
p=open("prt.txt","x")
data1=p.write("hey buddies its me....")
print(data1)
p.close()
"""


#write the information in a file
j=open("prt.txt","w")
info=j.write("hey wattsapp123")
j.close()
#append
j=open("prt.txt","a")
info=j.write("\n sorry its again me")
j.close()

"""
r+ is for read and write but the appended string will be in starting state
a+ is for same but the appending at last
"""

#WITH syntax advantage of this keyword with is that we may not write close() keyword..;
with open("prt.txt","r") as n:
    num=n.read(20)
    print(num)

#deleting file first import os module
#import os
#os.remove("delet.txt")
