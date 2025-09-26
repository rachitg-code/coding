from collections import defaultdict


def freqSort(arr, n):
    frq = defaultdict(int)

    for e in arr:
        frq[e] += 1

    ans = [(e, frq[e]) for e in arr]
    print(ans)
    ans.sort()
    print(ans)
    ans.sort(key=lambda x: x[1],reverse=True)
    print(ans)

    for e in ans:
        print(e[0],end=' ')


freqSort([6, 6, 4, 5, 5],5)