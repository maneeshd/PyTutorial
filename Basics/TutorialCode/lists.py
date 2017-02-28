nums = [91, 50, 54, 22, 30, 59]
N = len(nums)
for i in range(0, N):
    if i < N-1 and (nums[i] % 10) == 0:
        nums[i] ^= nums[i + 1]
        nums[i + 1] = nums[i] ^ nums[i + 1]
        nums[i] ^= nums[i + 1]
        i += 1
print(nums)
