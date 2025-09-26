v2 = [1, 5, 3, 7, 8, 2, 9, 4, 6]
k = 11
sum = 0
i = 0
j = 0
vOut = []

while j < len(v2):
    sum += v2[j]
    vOut.append(v2[j])

    while sum > k and i <= j:
        sum -= v2[i]
        vOut.pop(0)
        i += 1

    if sum == k:
        print("Subarray with sum", k, ":", vOut)
        break  # Remove this if you want to find all such subarrays

    j += 1
