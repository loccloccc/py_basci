nums = [10, 20, 30, 40, 50, 60]
total = 0
for i in range(len(nums)):
    if i % 2 == 0 :
        total += nums[i]

print(total)