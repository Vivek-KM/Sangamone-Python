Num=[]
Names=[]
Gender=[]
Regnum=[]
English=[]
Maths=[]
Physics=[]
Chemistry=[]
Biology=[]
Result=[]

f1=open ('Marks.txt','r')
for i in range(0,26,1):
    info=f1.readline()
    list1=info.split(",")
    Names.append(list1[0])
    Gender.append(list1[1])
    Regnum.append(list1[2])
    English.append(list1[3])
    Maths.append(list1[4])
    Physics.append(list1[5])
    Chemistry.append(list1[6])
    Biology.append(list1[7])
    Result.append(list1[8])

print(Names,end='\n')
print(Gender,end='\n')
print(Regnum,end='\n')
print(English,end='\n')
print(Maths,end='\n')
print(Physics,end='\n')
print(Chemistry,end='\n')
print(Biology,end='\n')
print(Result)
