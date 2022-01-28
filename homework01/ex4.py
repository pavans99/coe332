f = open('/usr/share/dict/words','r')
lines = f.readlines()[-10:]
for i in range(len(lines)):
    print(lines[i])
