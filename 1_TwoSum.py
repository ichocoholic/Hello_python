
nums = [2,7,11,15]
target = 9

def twoSum(nums,target):
    res = []
    for i in range(len(nums)):
        temp = target - nums[i]
        print (temp)
        if temp in nums and i!= nums.index(temp):
            a = nums.index(temp)
            res.append(i)
            res.append(a)
            break

    print (res)
    return res

twoSum(nums,target)
