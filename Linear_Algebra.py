def transpose(A):
  B=[]
  for j in range(len(A[0])):
    C = []
    for i in range(len(A)):
      C.append(A[i][j])
    B.append(C)
  return B

