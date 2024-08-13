f = open("nimet.txt", "r")
print(f.read()) 

rt = f.readline()

liv = len(rt)

for lr in rt:
    print(lr)