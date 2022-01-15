def penguin_AI(board, color):
  Y=[0,5,30,35,2,3,17,23,12,18,32,33,9,16,8,15,22,14,21,13,20,27,19,26,4,11,1,29,6,34,24,31,10,7,28,25]
  
  for _ in range(100):
    for i in Y:
      position=i
      if put_and_reverse(board,position,color):
        return position
  return 0
