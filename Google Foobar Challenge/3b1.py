def short_path(cur_x, cur_y, maze):
    width = len(maze[0])
    height = len(maze)
    dp = [[None for i in range(width)] for i in range(height)]
    dp[cur_x][cur_y] = 1

    arr = [(cur_x, cur_y)]
    while arr:
        x, y = arr.pop(0)
        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
          nx, ny = x + i[0], y + i[1]
          if 0 <= nx < height and 0 <= ny < width:
            if dp[nx][ny] is None:
                dp[nx][ny] = dp[x][y] + 1
                if maze[nx][ny] == 1 :
                  continue
                arr.append((nx, ny)) 
                  
    return dp

def solution(map):
  w = len(maze[0])
  h = len(maze)
  tb = short_path(0, 0, maze)
  bt = short_path(h-1, w-1, maze)
  dp = []

  result = 2 ** 32-1
  for i in range(h):
      for j in range(w):
          if tb[i][j] and bt[i][j]:
              result = min(tb[i][j] + bt[i][j] - 1, result)
  return result
