

def isMissingNum(arr):
    iter = 1
    end = len(arr)
    arr.sort()
    print(arr)
    while iter < end:
        if(arr[iter] - arr[iter - 1] > 1):
            print("Missing value : ", arr[iter]-1)
            return
        iter = iter + 1

    
        


if __name__ == '__main__':
    arr = [1, 2, 4, 6, 5, 3, 8]
    isMissingNum(arr)