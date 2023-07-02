class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])

        # print(m,n)

        first_row=False
        first_col=False

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    if i==0:
                        first_row=True
                    if j==0:
                        first_col=True

                    matrix[i][0]=0
                    matrix[0][j]=0
                    # print(matrix[i][0],matrix[0][j])

        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0

        # print(first_row,first_col)
                
        if first_row:
            for i in range(n):
                matrix[0][i]=0

        if first_col:
            for i in range(m):
                matrix[i][0]=0

