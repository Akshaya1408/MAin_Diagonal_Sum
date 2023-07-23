def diagonal_sum(mat,row,col):

    sum=0
    for i in range(row):
        sum+=mat[i][i]
    return sum

input_array=list(map(int,input().split()))
r=input_array[0]
c=input_array[1]
mat=[]
j=2
for i in range(r):
    mat.append(input_array[j:j+r])
    j+=r
# print(matrix)
print(diagonal_sum(mat,r,c))
