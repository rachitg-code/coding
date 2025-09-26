v2 = [1, 5, 3, 7, 8, 2, 9, 2, 6, 3]
k = 11

i = 0
j = 0
current_sum = 0
vOut = []
results = []

while j < len(v2):
    current_sum += v2[j]
    vOut.append(v2[j])

    # Shrink window from left if sum exceeds k
    while current_sum > k and i <= j:
        current_sum -= v2[i]
        vOut.pop(0)
        i += 1

    # If current sum equals target, store the subarray
    if current_sum == k:
        results.append(vOut.copy())

    j += 1

# Print all matching subarrays
for idx, r in enumerate(results):
    print(f"Subarray {idx+1} with sum {k}: {r}")
