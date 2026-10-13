#segment-tree
#segment-tree(seg<list<int>>)を返す
def segment(A):
    n = 1
    while n < len(A):
        n *= 2
    inf = 10 ** 12
    seg = [inf] * (2 * n)
    #葉に乗せる
    for i in range(len(A)):
        seg[i + n] = A[i]
    #根まで更新
    for i in range(n-1, 0, -1):
        seg[i] = min(seg[2 * i], seg[2 * i + 1])
    return seg

#segment-treeを用いて半開区間[l, r)の最小値を求める
#l, rはそれぞれ0-indexed
#最小値ans<int>を返す
def minSegment(l, r, seg):
    ans = 10 ** 12
    n = len(seg) // 2
    l += n
    r += n
    while l != r:
        if l % 2 == 1:
            ans = min(ans, seg[l])
            l += 1
        l //= 2
        if r % 2 == 1:
            r -= 1
            ans = min(ans, seg[r])
        r //= 2
    return ans

#segment-treeのseg[i]をxに変える
#iは0-indexed
#segment-tree(seg<list<int>>)を返す
def changeSegment(i, x, seg):
    n = len(seg) // 2
    i += n
    seg[i] = x
    i //= 2
    while i != 0:
        seg[i] = min(seg[2 * i], seg[2 * i + 1])
        i //= 2
    return seg