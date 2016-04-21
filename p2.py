def positive_sum(L):
    positive_sum =0
    for n in L:
        if n > positive_sum:
            positive_sum =n
    return positive_sum

L = [-1, 2, 14, 0, 0, 1]

print "Sum L:" , positive_sum(L)

M= [1,1,2,8,1]

print "Sum M:" , positive_sum(M)

N=[-1, -2, -3]

print "Sum N:" , positive_sum(N)