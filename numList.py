#Sum/Avergae Program
#Anthony Cross
#s1239598
num=float
numSum=0
numList=[]
for x in range(0,20):
    print("Input a number.")
    num=input()
    num=float(num)
    numList.append(num)
    numSum=numSum+num
print("The sum of your numbers is",numSum)
print("The average of your numbers is",(numSum/20))
