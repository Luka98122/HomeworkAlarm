def myFunc(t):
    print("myFunc called with " + str(t))
    if t == 1:
        print("t is 1")
    
    print("This is still in the function")
with open ("TEST.txt", 'r') as m:
    e =m.readlines()
    print(e)
    print("HERE")

gold = 100
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

with open("TEST.txt", 'wt') as t:
    t.write(str(gold)+'\n')
    for i in range(10):
        t.write(str(i) + "\n")
