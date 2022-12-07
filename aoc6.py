def subroutine(s):
    result= 0
    hashset = set()
    for i in range(len(s)):
        if(s[i] in hashset):
            for j in s[i-len(hashset): s[i-len(hashset):i].index(s[i])+(i-len(hashset))+1]:
                hashset.remove(j)


        hashset.add(s[i])
        if(len(hashset)==4): # for part 2 change 4 to 14
            result=i+1
            break

    return result


if __name__ == '__main__':
    f = open("input.txt", "r")
    print(subroutine(f.read()))
    f.close()