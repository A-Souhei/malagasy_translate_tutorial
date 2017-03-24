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


meerkat_file = open('meerkats.txt', 'r')
lastLine = ""
for line in meerkat_file:
	lastLine = line
meerkat_file.close()	
f = open('last_meerkat.txt' , 'w')	
f.write(lastLine + '\n')
f.close()

