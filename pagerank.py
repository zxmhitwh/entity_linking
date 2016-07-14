#coding=utf-8
# Filename:pr.py


S=[[0,0,0,0],[0.3333,0,0,1],[0.3333,0.5,0,0],[0.3333,0.5,1,0]] #原始矩阵
U=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]  #全部都为1的矩阵
f=[1,1,1,1]  #物征向量
alpha=0.85  # a 值 0-1之间的小数
n=len(S) #网页数


'''
aS a权重值 由google决定值大小，0-1之间，S为原始矩阵 
'''
def multiGeneMatrix(gene,Matrix):
    mullist=[[0]*len(Matrix) for row in range(len(Matrix))] #定义新的矩阵大小，初始化为0
    for i in range(0,len(Matrix)):
        for j in range(0,len(Matrix)):
            mullist[i][j] += Matrix[i][j]*gene
    return mullist 

'''
两个矩阵相加
'''
def addMatrix(Matrix1,Matrix2):
    if len(Matrix1[0])!=len(Matrix2):
        print "这两个矩阵无法相加..."
        return

    addlist=[[0]*len(Matrix1) for row in range(len(Matrix1))]    #定义新的矩阵大小
    for i in range(0,len(Matrix1)):
        for j in range(0,len(Matrix2)):
            addlist[i][j]=Matrix1[i][j]+Matrix2[i][j]
    return addlist
'''
矩阵与向量相乘
'''
def multiMatrixVector(m,v):
    rv=range(len(v))

    for row in range(0,len(m)):
        temp=0
        for col in range(0,len(m[1])):
            temp+=m[row][col]*v[col]
        rv[row]=temp
    return rv 

#公式
f1=multiGeneMatrix(alpha,S)
f2=multiGeneMatrix((1-alpha)/len(S[0]),U)
G=addMatrix(f1,f2)


print G  #google矩阵


#迭代过程
count=0
while(True):
    count=count +1
    pr_next=multiMatrixVector(G,f)
    print "第 %s 轮迭代" % count
    print str(round(pr_next[0],5)) +"\t" + str(round(pr_next[1],5)) + "\t" + str(round(pr_next[2],5)) + "\t" + str(round(pr_next[3],5))
    if round(f[0],5)==round(pr_next[0],5) and round(f[1],5)==round(pr_next[1],5) and round(f[2],5)==round(pr_next[2],5) and round(f[3],5)==round(pr_next[3],5):   #当前向量与上次向量值偏差不大后，停止迭
        break
    f=pr_next

print "Page Rank值已计算完成"