# 모든 요소를 0으로 초기화시킨 크기 6 x 6 인접 행렬
adjacency_matrix = [[0 for i in range(6)] for i in range(6)]

# 코드를 쓰세요
# 엣지 (영훈, 현승) 저장
adjacency_matrix[0][1] = 1
adjacency_matrix[1][0] = 1

# 엣지 (영훈, 동욱) 저장
adjacency_matrix[0][2] = 1
adjacency_matrix[2][0] = 1

# 엣지 (현승, 소원) 저장
adjacency_matrix[1][5] = 1
adjacency_matrix[5][1] = 1

# 엣지 (현승, 지웅) 저장
adjacency_matrix[1][3] = 1
adjacency_matrix[3][1] = 1

# 엣지 (동욱, 소원) 저장
adjacency_matrix[2][5] = 1
adjacency_matrix[5][2] = 1

# 엣지 (지웅, 소원) 저장
adjacency_matrix[3][5] = 1
adjacency_matrix[5][3] = 1

# 엣지 (지웅, 규리) 저장
adjacency_matrix[3][4] = 1
adjacency_matrix[4][3] = 1

# 엣지 (규리, 소원) 저장
adjacency_matrix[4][5] = 1
adjacency_matrix[5][4] = 1


# adjacency_matrix[0][1]=1
# adjacency_matrix[0][2]=1
# adjacency_matrix[1][3]=1
# adjacency_matrix[1][5]=1
# adjacency_matrix[2][5]=1
# adjacency_matrix[3][4]=1
# adjacency_matrix[3][5]=1
# adjacency_matrix[4][5]=1

# for i in range(6):
#     for j in range(6):
#         if adjacency_matrix[i][j] == 1:
#             adjacency_matrix[j][i] = 1 

print(adjacency_matrix)