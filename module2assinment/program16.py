string=input("Please Enter Your Own string :")
char=input("Please Enter your Own character :")

count=0
for i in range(len(string)):
    if(string[i]==char):
        count=count+1
print("The Total Number Of Times","has Occured",count)



