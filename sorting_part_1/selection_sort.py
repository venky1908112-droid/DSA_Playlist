a = [5, 3, 4, 2, 1]
n = len(a)
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if a[min_idx] > a[j]:
            min_idx = j
    a[min_idx], a[i] = a[i], a[min_idx]
print(a)