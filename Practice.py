def myFunc(t):
    print("myFunc called with " + str(t))
    if t == 1:
        print("t is 1")
    
    print("This is still in the function")

f = 2
print("Hello world")
print(f)

if f==1:
    print("f is one")
else:
    print("f is not one")

print("We are out of the if", end='')
myFunc(f)

for i in range(10):
    for k in range(i):
        print("o",end='')
    print("")

