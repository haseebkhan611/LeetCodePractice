

def isMissingNum(arr):
    length = len(arr)
    holder = [0] * (length+1)
    for i in arr:
        holder[i-1] = 1
    print(holder)

    index = 1

    for i in holder:
        if i == 0:
            print('Missing Val : ', index)
        index = index + 1

    
        


if __name__ == '__main__':
    arr = [1, 6, 4, 7, 5, 3, 8]
    isMissingNum(arr)