import sys

numCases = int(raw_input())
print("Number of cases: "+str(numCases))

while numCases > 0:
    N, K = map(int, raw_input().split())
    results = 0
    runOfZeroes = 0
    
    #print sys.stdin.read(1)
    #print sys.stdin.read(1)
    #print sys.stdin.read(1)
    
    char = sys.stdin.read(1)
    print("first char: "+char)
    while char != '\n':
        if char == ' ' or char == '':
            char = sys.stdin.read(1)
            continue
        print("not WS: "+char)
        bit = 1 if int(char) > K else 0
        
        if bit:
            if runOfZeroes > 0:
                results += 2 + runOfZeroes
            else:
                results += 1
            runOfZeroes = 0
        else:
            runOfZeroes += 1
            results += results
            
        char = sys.stdin.read(1)
        
    print results
    numCases -= 1