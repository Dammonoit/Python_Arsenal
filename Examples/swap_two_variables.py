print("Standard approach \n")

a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))

print("The value of a and b before swap is {0} and {1}\n".format(a,b))

temp=a
a=b
b=temp

print("The value of a and b after swap is {0} and {1} \n".format(a,b))

print("Python approach \n")

print("The value of a and b before swap is {0} and {1}\n".format(a,b))

a,b=b,a

print("The value of a and b after swap is {0} and {1} \n".format(a,b))
