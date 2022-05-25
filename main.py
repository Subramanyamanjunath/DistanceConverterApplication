# this program is to convert the distance values from kilometers to miles using suitable formula for conversion

distance = int(input("entered the travelled distance value to convert : "))
unit = input("enter input type i.e k for kms or M for miles: ")


if unit == "k":
     converted = distance/1.609
     print(f"you have covered{converted} miles")

elif unit.upper()=="M":
     converted = distance * 1.609
     print(f" you have covered {converted} kms")

else:
    print("wrong input")


