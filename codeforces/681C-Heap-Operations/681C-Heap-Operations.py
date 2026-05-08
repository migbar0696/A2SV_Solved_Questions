import sys
input = sys.stdin.readline

import heapq

n = int(input())


arr = []
ans = []

for _ in range(n):
    
    opt = input().split()
    
    if opt[0] == "insert":
        ans.append(opt[0] +" " +opt[1])
        heapq.heappush(arr, int(opt[1]))
    elif opt[0] == "removeMin":
        if arr:
            ans.append(opt[0])
            heapq.heappop(arr)
        else:
            ans.append("insert 1")
            ans.append(opt[0])
    elif opt[0] == "getMin":
        if arr:
            if arr[0] > int(opt[1]):
                ans.append("insert" +" " +opt[1])
                heapq.heappush(arr, int(opt[1]))
                ans.append(opt[0] +" " +str(arr[0]))
            
            elif arr[0] == int(opt[1]):
                ans.append(opt[0] +" " +str(arr[0]))
            
            else:
                while arr and arr[0] < int(opt[1]):
                    heapq.heappop(arr)
                    ans.append("removeMin")
                if arr and arr[0] == int(opt[1]):
                    ans.append(opt[0] +" " +opt[1])
                elif arr and arr[0] > int(opt[1]):

                    ans.append("insert" +" " + opt[1])
                    heapq.heappush(arr, int(opt[1]))
                    ans.append(opt[0] +" " +str(arr[0]))
                elif not arr:
                    ans.append("insert" +" " +  opt[1])
                    heapq.heappush(arr, int(opt[1]))
                    ans.append(opt[0] +" " + str(arr[0]))
                    
            
        else:
            ans.append("insert"+ " " + opt[1])
            heapq.heappush(arr, int(opt[1]))
            ans.append(opt[0]+ " " + str(arr[0]))
        
    
print(len(ans))
for each in ans:
    print(each)