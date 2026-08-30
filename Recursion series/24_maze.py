# count the no of possible ways to reach end(1,1) from start(3,3)
# Directions allowed: D, R
# (3,3) (3,2) (3,1)
# (2,3) (2,2) (2,1)
# (1,3) (1,2) (1,1)

def maze_path_count(r, c):
    if r==1 or c==1:
        return 1

    if r > 1:
        left = maze_path_count(r-1, c)
    if c > 1:
        right = maze_path_count(r, c-1)

    return left + right

# return list of all the path directions of a maze
# Directions allowed: D, R
# (3,3) (3,2) (3,1)
# (2,3) (2,2) (2,1)
# (1,3) (1,2) (1,1)

def maze_path(r, c, p):
    if r==1 and c==1:
        res = [p]
        return res
    path = []
    if r > 1:
        path.extend(maze_path(r-1, c, p + 'D'))
    if c > 1:
        path.extend(maze_path(r, c-1, p + 'R'))
    return path

# return list of all the path directions of a maze with obstacle from (0,0) to (2,2)
# Directions allowed: D, R
# (0,0) (0,1) (0,2)
# (1,0)       (1,2)
# (2,0) (2,1) (2,2)

def maze_path_with_obstacle(r, c, obstacle, p):
    if r==len(obstacle)-1 and c==len(obstacle[0])-1:
        res = [p]
        return res
    path = []

    if not obstacle[r][c]:
        return ""

    if r < len(obstacle) - 1:
        path.extend(maze_path_with_obstacle(r+1, c, obstacle, p + 'D'))
    if c < len(obstacle[0]) - 1:
        path.extend(maze_path_with_obstacle(r, c+1, obstacle, p + 'R'))
    return path

# return list of all the path directions of a maze from (0,0) to (2,2)
# Directions allowed: D, R, U, L
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)

def all_path_of_maze(r, c, maze_map, p):
    if r == len(maze_map)-1 and c == len(maze_map[0])-1:
        print(p)
        return
    if not maze_map[r][c]:
        return
    maze_map[r][c] = False
    if r < len(maze_map)-1:
        all_path_of_maze(r+1, c, maze_map, p + 'D')
    if c < len(maze_map[0]) - 1:
        all_path_of_maze(r, c+1, maze_map, p + 'R')
    if r > 0:
        all_path_of_maze(r-1, c, maze_map, p + 'U')
    if c > 0:
        all_path_of_maze(r, c-1, maze_map, p + 'L')

    # Now all the path will be marked as False, hence next recursion function can't able to find a correct path.
    # So, before the func gets removed, also remove the changes that were made by that function.
    # This is known as "back tracking"
    maze_map[r][c] = True


# we have to return the path matrix and path directions
# we pass an additional 3*3 matrix which initially holds 0 and variable step to count the current step
# need to update the matrix with current step count.
# And before the func gets removed, also change the matrix count back to 0 (Back Tracking)

def all_path_with_matrix(r, c, maze_map, matrix, step, p):
    if r == len(maze_map)-1 and c == len(maze_map[0])-1:
        matrix[r][c] = step
        for row in matrix:
            print(row)
        print(p)
        print()
        return
    if not maze_map[r][c]:
        return
    maze_map[r][c] = False
    matrix[r][c] = step
    if r < len(maze_map)-1:
        all_path_with_matrix(r+1, c, maze_map, matrix, step+1, p + 'D')
    if c < len(maze_map[0]) - 1:
        all_path_with_matrix(r, c+1, maze_map, matrix, step+1, p + 'R')
    if r > 0:
        all_path_with_matrix(r-1, c, maze_map, matrix, step+1, p + 'U')
    if c > 0:
        all_path_with_matrix(r, c-1, maze_map, matrix, step+1, p + 'L')

    maze_map[r][c] = True
    matrix[r][c] = 0

print(maze_path_count(3, 3))
print(maze_path(3, 3, ""))
obstacle_map = [
    [True, True, True],
    [True, False, True],
    [True, True, True]
]
print(maze_path_with_obstacle(0, 0, obstacle_map,  ""))
m_map = [
    [True, True, True],
    [True, True, True],
    [True, True, True]
]
print(all_path_of_maze(0, 0, m_map,  ""))
empty_matrix = [[0 for _ in range(3)] for _ in range(3)]
print(all_path_with_matrix(0, 0, m_map, empty_matrix, 1, ""))