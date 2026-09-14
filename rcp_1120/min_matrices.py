def main():
    t = int(input())
    for _ in range(t):
        n,k = list(map(int, input().split()))
        if k < n or k>=2*n:
            print(-1)
            continue
        print_matrix(get_matrix(n,k))

def get_matrix(n,k):
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    diags =2*n-k
    nums = range(1, n**2 +1)
    i = 0
    j = 0
    for _ in range(i,diags):
        matrix[i][i] = nums[i]
        i+=1
        j+=1
    j-=1
    
    for _ in range(n-diags):
        matrix[j][i] = nums[i]
        i+=1
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == 0:
                matrix[r][c] = nums[i]
                i+=1
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for el in row:
            print(str(el), end= " ")
        print()
main()