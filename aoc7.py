import collections
class System:
    def __init__(self):
        self.dirs=collections.defaultdict(dict)
        self.start=self.dirs
        self.dirs["/"] = {'file':0}
        self.path=["/"]
        self.res=0
        self.total=0
        self.req=float('inf')

    def run(self, messg):
        if messg.startswith("$"):
            if(messg[2:4]=="cd"):
                if(messg[5:]==".."):
                    self.path.pop()
                elif(messg[5:]=="/"):
                    self.path=["/"]
                else:
                    self.path.append(messg[5:])

        elif messg.startswith("dir"):
            ptr = self.dirs["/"]
            for i in range(1,len(self.path)):
                ptr=ptr[self.path[i]]
            ptr[messg[4:]] = {'file':0}

        
        else: # file creation
            ptr = self.dirs["/"]
            for i in range(1,len(self.path)):
                ptr=ptr[self.path[i]]
            ptr['file']+=int("".join([x for x in messg if x.isdigit()]))

    def calculate(self, pathh):
        countt = int(pathh["file"])
        for i in pathh:
            if(i!="file"):
                countt+=self.calculate(pathh[i])
        if(countt<=100000):
            self.res+=countt
        return countt

    def calculate_total(self, pathh):
        countt = int(pathh["file"])
        for i in pathh:
            if(i!="file"):
                countt+=self.calculate_total(pathh[i])
        self.res+=countt
        self.total = countt - 40000000
        return countt

    def calculate_minimum(self, pathh):
        countt = int(pathh["file"])
        for i in pathh:
            if(i!="file"):
                countt+=self.calculate_minimum(pathh[i])
        self.res+=countt

        if(countt>self.total):
            self.req=min(self.req, countt)

        return countt




            



if __name__ == '__main__':
    system = System()
    f=open("input7.txt", "r")
    for i in f.readlines():
        system.run(i.strip())
    # part 1
    # system.calculate(system.dirs["/"])
    # print(system.res)
    # part 2
    system.calculate_total(system.dirs["/"])
    system.calculate_minimum(system.dirs["/"])
    print(system.req)
    
    f.close()