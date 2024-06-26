

# algo:
# if 

def twoSumHash(arr1, k):
    hashTable = {}
    for i, nums in enumerate(arr1):
        x = k - nums
        if x in hashTable:
            print(f"Found @ {hashTable[x]}, {x}")
            print(f"{hashTable}")
            return
        hashTable[nums] = i
    print('Not Found')
    return

def twoSum1(arr, k):
    for i in range(len(arr)):
        firstNum = arr[i]
        for j in range(1,len(arr)):
            secNum = arr[j]
            if firstNum + secNum == k:
                print(f"Target found. @ {i},  {j}")
                return
                

def twoSum(arr1, k):
    arr = sorted(arr1)
    i = 0
    j = len(arr) - 1
    while True:
        if arr[i] + arr[j] > k:
            j = j - 1
        elif arr[i] + arr[j] < k:
            i = i + 1
        elif arr[i] + arr[j] == k:
            print(i, j)
            return False

if __name__ == '__main__':
    arr = [2,3,4]
    target = 6
    # twoSum(arr, target)
    twoSumHash(arr, target)