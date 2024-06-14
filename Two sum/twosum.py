

# algo:
# if 

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
    arr = [3,2,4]
    target = 6
    twoSum(arr, target)