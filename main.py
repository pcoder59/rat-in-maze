def run_maze(maze: list[list[int]], i: int, j: int, solutions: list[list[int]]) -> bool:
	size = len(maze)
	#Final Check Point
	if i == j == (size - 1):
		solutions[i][j] = 1
		return True
	#Check Lower Bounds
	lower_flag = (not (i < 0)) and (not (j < 0))
	#Check Upper Bounds
	upper_flag = (i < size) and (j < size)
	
	if lower_flag and upper_flag:
		#Check Already Visited and Block Points
		block_flag = (not (solutions[i][j])) and (not (maze[i][j]))
		if block_flag:
			#Check Visited
			solutions[i][j] = 1
			
			#Check For Dierctions
			if(
				run_maze(maze, i+1, j, solutions)
				or run_maze(maze, i, j+1, solutions)
				or run_maze(maze, i-1, j, solutions)
				or run_maze(maze, i, j-1, solutions)
			):
				return True
			
			solutions[i][j] = 0
			return False
	return False

def solve_maze(maze: list[list[int]]) -> bool:
	size = len(maze)
	solutions = [[0 for _ in range(size)] for _ in range(size)]
	solved = run_maze(maze, 0, 0, solutions)
	
	if(solved):
		print("\n".join(str(row) for row in solutions))
	else:
		print("No Solution Exists!")
	return solved 
				 
if __name__ == "__main__":
	solved = solve_maze([[0, 1, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1], [0, 0, 1, 0, 0], [1, 0, 0, 1, 0]])
	print(solved)