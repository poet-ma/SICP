#计算立方和
def cube(x):
    return x*x*x

#计算从a到b的所有整数之和
def SumIntegers(a, b):
    if a > b:
        return 0
    else:
        return a + SumIntegers(a + 1, b)
       
#计算从a到b的所有整数的立方之和       
def SumCubes(a, b):
    if a > b:
        return 0
    else:
        return cube(a) + SumCubes(a+1, b)


##以上为两个求和函数，其实二者的本质在于表达求和本身，能否从本质上去表达求和呢，就像数学一样f(n) = f(a)  + .... + f(b);注n从a到b
##可以考虑将输入定义为各种f，输出是具体的求和函数
#抽象出求和函数
def Sum(function, a, next, b):
    if a > b:
        return 0
    else:
        return function(a) + Sum(function, next(a), next, b)


def inc(n):
    return n + 2

next = inc
function = cube  
def SumCubes_another(a, b):
    return Sum(function, a, next, b)
f = SumCubes_another

##这里得到一个函数f, 这个函数其实跟函数SumCubes所表达的本质是一样的
print f(1, 3)








        





