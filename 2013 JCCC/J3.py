F = open("C:\\Users\jamie\Downloads\J3\j3.1.in", "r") 
year = int(F.readline())


def isdistinct (x):

    nums = []

    while (x != 0):
        nums.append(x%10)
        x = x//10

    nums.sort()

    for i in range (1, len(nums),1):
        if (nums[i] == nums[i-1]):
            return False
    
    return True 

nums = year 
nums = nums + 1

distinct = isdistinct(nums) 

while(distinct == False):
    nums += 1
    distinct = isdistinct(nums)

print(nums) 