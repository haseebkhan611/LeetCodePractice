# Statement and example

```
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
````


# algorithm

Assume an array with size [0 ... n-1]

Any 2 nums should sum up to k

pointers: i, j
i will start from 0 and move towards right side
j will start from n-1 and move towards left side

if arr[i] - arr[j] >= k:
    j--
elif arr[i] - arr[j] < k:
    i++
elif arr[i] - arr[j] == k:
    return [i, j]
    