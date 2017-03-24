"""
In the file we are reading a file line-by-line and printing it on the screen.
Exercise:
1. Change program to print only words from the last line.
2. Write words from the last line of the file `meerkats.txt` into another file called `last_meerkat.txt`
To write something to a file you can use following code:
    f = open('myfile', 'w')
    f.write('Line in a file\n')
    f.close()

"""
n = sum(1 for line in open("meerkats.txt")) - 1
l = '';
fp = open("meerkats.txt")
for i, line in enumerate(fp):
    if i == n:
        print(line)
        l = line
    else:
        continue
fp.close()
f = open('last_meerkat.txt','w')
f.write(l + '\n')
f. close()
