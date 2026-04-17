def merge(left, right):
        global cnt
        arr = []
        
        if left[0] > right[0]:
            right += left
            arr.extend(right)
            cnt += 1
        else:
            left += right
            arr.extend(left)

        return arr
        
        
    def mergesort(left, right, arr):
        if left== right:
            return [arr[left]]
        mid = left + (right - left)//2
        
        left = mergesort(left, mid, listn)
        right = mergesort(mid + 1, right, listn)
        
        return merge(left, right)

    

    # print(listn)
    if sorted(listn) == mergesort(0, len(listn) - 1, listn):
        print(cnt)
    else:
        print(-1)