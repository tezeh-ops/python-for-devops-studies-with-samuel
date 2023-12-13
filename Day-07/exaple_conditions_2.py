
import sys

type = sys.argv[1]

if type == "t2.micro":
    print("ok, we will create the t2.micro instane but it will cahrge you $2 a day ")

elif type == "t2.midium":
    print("ok, we will create the t2.midium instane but it will cahrge you $4 a day ")

elif type == "t2x.large":
    print("ok, we will create the t2.large instane but it will cahrge you $5 a day ")


else:
    print("the instance type is not valid")