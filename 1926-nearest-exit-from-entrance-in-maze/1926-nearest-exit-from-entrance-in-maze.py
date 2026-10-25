class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])

        q = deque()
        q.append([entrance[0],entrance[1],0])
        visited=set()
        while q:
            #print(q)
            for i in range(len(q)):
                r, c, steps = q.popleft()
                if (r == (ROWS-1) and maze[r][c] == ".") or (c == (COLS-1) and maze[r][c] == ".") or (r == 0 and maze[r][c] == ".") or (c == 0 and maze[r][c] == ".") :
                    if r !=entrance[0] or c != entrance[1]: 
                        return steps
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    rows, cols = r + dr, c + dc
                    if rows < 0 or rows >= ROWS or cols < 0 or cols >= COLS or maze[rows][cols] == '+' or (rows,cols) in visited:
                        continue
                    else:
                        q.append([rows,cols,steps+1])
                        visited.add((rows,cols))

        return -1
