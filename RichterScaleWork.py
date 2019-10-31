#Anthony Cross
#s1239598
RichterInput=float
while RichterInput!=-99:
    print("What was the magnitude of the earthquake? Enter the value or -99 to quit.")
    RichterInput=input()
    RichterInput=float(RichterInput)
    if RichterInput!=-99:
        if RichterInput<0:
            print("Value must be greater than 0.")
        elif RichterInput>=8.0:
            print("Most structures fall.")
        elif RichterInput>=7.0:
            print("Many buildings destroyed.")
        elif RichterInput>=6.0:
            print("Many buildings considerably damaged, some collapse.")
        elif RichterInput>=4.5:
            print("Damage to poorly constructed buildings.")
        else:
            print("No destruction of buildings.")
print("Goodbye.")
