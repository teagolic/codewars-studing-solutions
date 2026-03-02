def next_gen(cells: list[list[int]]):
  now_gen = [[0 for y in range(len(cells))] for x in range(len(cells))]

  for i in range(len(cells)):
    for j in range(len(cells[i])):
      neighbor = 0

      for k in range(max(0, i-1),min(i+2, len(cells))):
        for m in range(max(0, j-1),min(j+2, len(cells[i]))):
          if not((k == i and m == j)) and cells[k][m] == 1:
            neighbor += 1

      if cells[i][j] == 0:
        if neighbor == 3:
          now_gen[i][j] = 1

      else:
        if neighbor < 2 or neighbor > 3:
          now_gen[i][j] = 0
        else:
          now_gen[i][j] = 1

  return now_gen
