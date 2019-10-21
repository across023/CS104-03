nameList=[]
nameNeeded=""
inputName=""
keepSearch=True
print("Please input 10 names.")
for x in range(0,10):
    inputName=input()
    nameList.append(inputName)
while keepSearch==True:
    print("Input the name you would like to look for, grammar matters.")
    print("Type 'end' to stop.")
    nameNeeded=input()
    if nameNeeded=="end":
        keepSearch=False
    elif nameNeeded in nameList:
        print(nameNeeded,"is on the list.")
    else:
        print(nameNeeded,"is not on the list.")
print("Goodbye.")
