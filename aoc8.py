import collections
def getlines():
    with open("input8.txt") as f:
        return list(map(lambda x: x.strip(), f.readlines()))
        
def get_visible():
    lines = getlines()
    row = len(lines)
    result= 4 * (row-1)
    line = [[y for y in x] for x in lines]
    # this part can be done in a more efficient way by passing through the rows and columns once and logging the known visible tree using a set but I wanted to try out the ripple effect 
    def ripple(i, j):
        left=list(map(lambda x: int(x)<int(line[i][j]), [line[i][x] for x in range(j-1, -1, -1)]))
        right=list(map(lambda x: int(x)<int(line[i][j]), [line[i][x] for x in range(j+1, row)]))
        top=list(map(lambda x: int(x)<int(line[i][j]), [line[x][j] for x in range(i-1, -1, -1)]))
        bottom=list(map(lambda x: int(x)<int(line[i][j]), [line[x][j] for x in range(i+1, row)]))
        return all(left) or all(right) or all(top) or all(bottom)


    for i in range(1, len(line)-1):
        for j in range(1, len(line[0])-1):
            if ripple(i,j):
                print(i,j)
                result+=1
    print(result)

def get_max():
    lines=  getlines()
    row=len(lines)
    line = [[y for y in x] for x in lines]
    def calc(i, j):
        left=0
        for x in range(j-1,-1,-1):
            left+=1
            if(line[i][x] >= line[i][j]):
                break
        right=0
        for x in range(j+1,row):
            right+=1
            if(line[i][x] >= line[i][j]):
                break
        top=0
        for x in range(i-1, -1, -1):
            top+=1
            if(line[x][j] >= line[i][j]):
                break
        bottom=0
        for x in range(i+1,row):
            bottom+=1
            if(line[x][j] >= line[i][j]):
                break
        return top*bottom*left*right

    maximum=calc(1, 1)
    for i in range(1, len(line)-1):
        for j in range(1, len(line[0])-1):
            maximum=max(maximum, calc(i,j))
    print(maximum)
    
    




if __name__ == '__main__':
    # part 1
    # get_visible()
    # part 2
    get_max()