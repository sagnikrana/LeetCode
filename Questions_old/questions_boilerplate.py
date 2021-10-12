nums = [3,2,2,3]
val = 3

# for index in range(len(nums)):
#     if index != len(nums)-1:
#         if nums[index] == val:
#             del nums[index]
index = 0
while(index != len(nums)):
    if nums[index] == val:
        del nums[index]
    else:
        index += 1

print(nums)