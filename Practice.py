print('Hello world')
gold = 100

try:
    with open ("TEST.txt", 'r') as m:
        e = m.readlines()
        print(e)
        print
        
        gold = int(e[0]) * 2
        
except FileNotFoundError:
    print('File not found')

print('File read')


with open("TEST.txt", 'wt') as t:
    
    t.write(str(gold)+'\n')
   

    for i in range(10):
        t.write(str(i) + "\n")

print(gold)