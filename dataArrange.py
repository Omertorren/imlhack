from data.getData import *
a,b = getData()
f = open("data.csv","w")

for word in a[:1000]:
    f.write("'%s'\t1\n"%word)

for word in b[:1000]:
    f.write("'%s'\t-1\n"%word)

t = open("dataTest.csv","w")

for word in a[1000:]:
    t.write("'%s'\t1\n"%word)

for word in b[1000:]:
    t.write("'%s'\t-1\n"%word)