def beginner_tactics(board, color, lst): # 初心者ムーブ
  lst_quiet = [-7, -6, -5, -1, +1, +5, +6, +7]
  
  min_emp = 8
  for quiet in lst:
    if put_and_reverse(board, quiet, color):
      emp = 0
      for _ in range(len(lst_quiet)):
        neighbor = quiet + lst_quiet[_] # 隣り合うマスの座標
        if neighbor >= 0 and neighbor <= 35:
          if put_and_reverse(board, neighbor, BLACK) or put_and_reverse(board, neighbor, WHITE):
            emp += 1 # 空白の数を数える
      if emp < min_emp:
        min_emp = emp # 隣り合うマスに空白が少なければ min_emp を更新
        QUIET = quiet

  try:
    return QUIET # 隣に空白マスが少ないマスの座標を出力
  except:
    return "Error" # ない場合は "Error" と出力して次の動作へ進む

def beginner_AI(board, color):
  lst_corner = [0, 5, 30, 35] # 角 オススメLv.5
  lst_edge = [2, 3, 12, 17, 18, 23, 32, 33] # 壁沿い オススメLv.4
  lst_circle = [8, 9, 13, 16, 19, 22, 26, 27] # 中の方 オススメLv.3
  lst_C = [1, 4, 6, 11, 24, 29, 31, 34] # Cライン(角の上下左右隣) オススメLv.2
  lst_X = [7, 10, 25, 28] # Xライン(角の斜め隣) オススメLv.1

  lst_all = [lst_corner, lst_edge, lst_circle, lst_C, lst_X]

  for i in range(len(lst_all)):
    position = beginner_tactics(board, color, lst_all[i])
    if position == "Error":
      pass
    else:
      return position

  return 0