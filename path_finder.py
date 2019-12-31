import queue
import time
# from collections import deque


def create_maze():
    maze = []
    maze.append(['#', 'A', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#'])
    maze.append(['#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'])
    maze.append(['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', '#'])
    maze.append(['#', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', '#'])
    maze.append(['#', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ', '#', ' ', '#'])
    maze.append(['#', ' ', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#'])
    maze.append(['#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#'])
    maze.append(['#', ' ', ' ', '#', '#', '#', '#', ' ', '#', 'B', ' ', ' ', ' ', '#', ' ', '#'])
    maze.append(['#', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#', '#'])
    maze.append(['#', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#'])
    maze.append(['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#'])

    return maze


def print_maze_done(maze, moves):
    start = find_start_point(maze)
    road = calculate_moves(start, moves)[2]
    print_road_on_maze(maze, road)
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            print(col + " ", end="")
        print()


def print_road_on_maze(maze, road):
    print("Shortest path : "+str(road))
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if (i, j) in road[:-1]:
                maze[i][j] = 'ₒ'


def is_move_valid(maze, moves):
    start = find_start_point(maze)
    dest = calculate_moves(start, moves)
    if not (0 <= dest[0] < len(maze) and 0 <= dest[1] < len(maze[0])):
        return False
    elif maze[dest[0]][dest[1]] == '#':
        return False

    return True


def is_reached_destination(maze, moves):
    start = find_start_point(maze)
    dest = calculate_moves(start, moves)
    if maze[dest[0]][dest[1]] == 'B':
        print_maze_done(maze, moves)
        return True

    return False


def find_start_point(maze):
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if maze[i][j] == 'A':
                return [i, j]


def calculate_moves(start, moves):
    road = []
    for move in moves:
        if move == 'R':
            start[1] += 1
        elif move == 'L':
            start[1] -= 1
        elif move == 'U':
            start[0] -= 1
        elif move == 'D':
            start[0] += 1
        road.append((start[0], start[1]))
    return [start[0], start[1], road]


def bfs_algorithm():
    q = queue.Queue()
    q.put("")
    to_add = ''
    maze = create_maze()
    start_time = time.time()
    while not is_reached_destination(maze, to_add):
        to_add = q.get()
        for dir in ['R', 'L', 'U', 'D']:
            add = to_add + dir
            if is_move_valid(maze, add):
                q.put(add)
        if time.time() - start_time > 15:
            print("No path found")
            break
    print("Calculation time : " + str(time.time() - start_time)+" seconds")


# def dfs_algorithm():
#     q = queue.Queue()
#     q.put("")
#     to_add = ''
#     maze = create_maze()
#     visited = [[False for i in range(len(maze))] for j in range(len(maze[0]))]
#     start_time = time.time()
#     while not is_reached_destination(maze, to_add):
#         to_add = q.get()
#         for dir in ['R', 'L', 'U', 'D']:



if __name__ == '__main__':
    bfs_algorithm()
    # dfs_algorithm()