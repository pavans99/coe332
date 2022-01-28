f = open('/usr/share/dict/words','r')
for line in f:
    if (line[0:3]=='pyt'):
        print(line)

