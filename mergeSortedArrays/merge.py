

def merge(nums1, m, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if(n == 0):
        # nums[0] = nums2[0]
        return
    if(m == 0):
        nums1[0] = nums2[0]
        return
    dummy = [0] * (m+n)
    idx = len(dummy) - 1
    arr1 = [x for x in nums1 if x != 0]
    # print('length : ', idx)
    x = n - 1
    y = m - 1
    # print('arr1 : ', arr1)
    # print('nums2 : ', nums2)
    
    while x >= 0 and y >= 0:
        # print(idx)
        if(arr1[x] >= nums2[y]):
            # print('easter egg 1. X :  %d, Value %d', x, arr1[x])
            nums1[idx] = arr1[x]
            x -= 1
            # print(dummy)
        else:
            # print('easter egg 2. Y : %d, Value %d', y, nums2[y])
            nums1[idx] = nums2[y]
            y -= 1
            # print(dummy)
        
        
        # print('idx : ', idx)
        idx -= 1
    
    
    while x >= 0:
        # print('easter egg 3')
        # print(idx)
        # print('n and idx', x, idx)
        nums1[idx] = arr1[x]
        x -= 1
        idx -= 1
        # print(dummy)
    
    # while y > 0:
    
    # print(dummy)
    # for i in range(idx):
    #     nums1[i] = dummy[i]
    print(nums1)

if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    merge(nums1, m, nums2, n)