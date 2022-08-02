prison=["c","c","c","c","c","c","c","c","c","c"]
print("Initial position of all prison",prison)
for i in range(0,10,1):
    prison[i]="O"
print("Prison position after round 1",prison)
for i in range(1,10,2):
    prison[i]="C"
print("Prison position after round 2",prison)
for i in range(2,10,3):
    if prison[i]=="C":
        prison[i]="O"
    else:
            prison[i]="C"
print("Prison position after round 3",prison)
for i in range(3,10,4):
    if prison[i]=="C":
        prison[i]="O"
    else:
        prison[i]="C"
print ("Prison position after round 4",prison)
for i in range(4,10,5):
    if prison[i]=="C":
        prison[i]="O"
    else:
        prison[i]="C"
print ("Prison position after round 5",prison)
for i in range(5,10,6):
    if prison[i]=="C":
        prison[i]="O"
    else:
        prison[i]="C"
print ("Prison position after round 6",prison)
for i in range(6,10,7):
    if prison[i]=="C":
        prison[i]="O"
    else:
        prison[i]="C"
print ("Prison position after round 7",prison)
for i in range(7,10,8):
    if prison[i]=="C":
        prison[i]="O"
    else:
        prison[i]="C"
print ("Prison position after round 8",prison)
for i in range(8,10,9):
    if prison[i]=="C":
        prison[i]="O"
    else:
        prison[i]="C"
print ("Prison position after round 9",prison)
for i in range(9,10,10):
    if prison[i]=="C":
        prison[i]="O"
    else:
        prison[i]="C"
print ("Prison position after round 10",prison)

print("The lucky prisoners are: ")
for i in range(0,10,1):
    if prison[i]=="O":
        print("Cell no: ",i+1)
        
print("The unlucky prisoners are: ")
for i in range(0,10,1):
    if prison[i]=="C":
        print("Cell no: ",i+1)
        

        
  









    
    
    
