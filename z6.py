def main(x):
    x0 = {1970: 0, 2002: 1}
    x1 = {'ARC': 1, 'CLICK': 2}
    x2 = {'CLICK': 5, 'OOC': 0}
    x3 = {1963: 0, 1989: 1, 2012: 2}
    pruf1 = x[3] == 1989 and x[2] == 'OOC'
    pruf1 = pruf1 or x[3] == 2012 and x[2] == 'CLICK'
    pruf0 = x[3] == 1963
    pruf0 = pruf0
    pruf1 = pruf1
    dop3 = x[2] == 'CLICK' and x[3] == 1989
    dop3 += (x[3] == 2012 and x[2] == 'OOC') * 2
    res = x0[x[0]] * pruf0
    res += x1[x[1]] * pruf1
    res += x2[x[2]] + x3[x[3]]
    res += dop3
    print(pruf0, pruf1)
    return res


print(main([2002, 'ARC', 'OOC', 1989, 1970]))
print(main([2002, 'CLICK', 'OOC', 1963, 1970]))
print(main([1970, 'CLICK', 'CLICK', 2012, 1970]))
print(main([1970, 'CLICK', 'CLICK', 1963, 1970]))
print(main([2002, 'CLICK', 'CLICK', 1963, 1970]))

