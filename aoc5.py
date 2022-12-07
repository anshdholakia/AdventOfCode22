s = ['HTZD', 'QRWTGCS', 'PBFQNRCH', 'LCNFHZ', 'GLFQS', 'VPWZBRCS', 'ZFJ', 'DLVZRHQ', 'BHGNFZLD']
f = open("input5.txt", 'r')
for i in [[int(k.strip().split(" from ")[0][5:]), int(k.split(" from ")[1].strip
().split(" to ")[0]), int(k.strip().split(" from ")[1].split(" to ")[1])] for k in f.readlines()]:
    s[i[2]-1]+=s[i[1]-1][-i[0]:][::-1] # for part 2 remove [::-1]
    s[i[1]-1]=s[i[1]-1][:-i[0]]


print("".join([x[-1] for x in s]))
f.close()
