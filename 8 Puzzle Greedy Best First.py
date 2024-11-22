import heapq
import random
import time

class PuzzleState:
    def __init__(self, tiles, empty_position, steps=0, previous=None):
        self.tiles = tiles
        self.empty_position = empty_position
        self.steps = steps
        self.previous = previous
        self.heuristic = self.calculate_manhattan_distance()

    def calculate_manhattan_distance(self):
        distance = 0
        for row in range(3):
            for col in range(3):
                value = self.tiles[row][col]
                if value != 0:
                    goal_row = (value - 1) // 3
                    goal_col = (value - 1) % 3
                    distance += abs(goal_row - row) + abs(goal_col - col)
        return distance

    def find_possible_moves(self):
        moves = []
        x, y = self.empty_position
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_tiles = [row[:] for row in self.tiles]
                new_tiles[x][y], new_tiles[new_x][new_y] = new_tiles[new_x][new_y], new_tiles[x][y]
                moves.append(PuzzleState(new_tiles, (new_x, new_y), self.steps + 1, self))
        return moves

    def __lt__(self, other):
        return self.heuristic < other.heuristic

    def is_goal_state(self):
        return self.tiles == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def print_board(self):
        for row in self.tiles:
            print(" ".join(str(tile) if tile != 0 else " " for tile in row))
        print()

def count_inversions(tiles):
    flat_tiles = [num for row in tiles for num in row if num != 0]
    inversions = 0
    for i in range(len(flat_tiles)):
        for j in range(i + 1, len(flat_tiles)):
            if flat_tiles[i] > flat_tiles[j]:
                inversions += 1
    return inversions

def check_solvable(tiles):
    return count_inversions(tiles) % 2 == 0

def create_random_puzzle():
    numbers = list(range(9))
    random.shuffle(numbers)
    board = [numbers[i:i+3] for i in range(0, 9, 3)]
    while not check_solvable(board):
        random.shuffle(numbers)
        board = [numbers[i:i+3] for i in range(0, 9, 3)]
    empty_position = next((i, row.index(0)) for i, row in enumerate(board) if 0 in row)
    return board, empty_position

def solve_puzzle(start_board):
    empty_position = None
    for row in range(3):
        for col in range(3):
            if start_board[row][col] == 0:
                empty_position = (row, col)
                break
    initial_state = PuzzleState(start_board, empty_position)
    priority_queue = []
    heapq.heappush(priority_queue, initial_state)
    visited_states = set()
    visited_states.add(tuple(tuple(row) for row in start_board))
    move_counter = 0
    nodes_explored = 0
    max_queue_size = 0
    start_time = time.time()
    solution_path = []
    while priority_queue:
        max_queue_size = max(max_queue_size, len(priority_queue))
        current_state = heapq.heappop(priority_queue)
        nodes_explored += 1
        if current_state.is_goal_state():
            while current_state:
                solution_path.append(current_state)
                current_state = current_state.previous
            solution_path.reverse()
            break
        for move in current_state.find_possible_moves():
            state_tuple = tuple(tuple(row) for row in move.tiles)
            if state_tuple not in visited_states:
                visited_states.add(state_tuple)
                heapq.heappush(priority_queue, move)
    end_time = time.time()
    if solution_path:
        print("Solution Path:")
        for state in solution_path:
            print(f"Move {move_counter}:")
            state.print_board()
            move_counter += 1
        return {
            "steps": len(solution_path) - 1,
            "nodes_explored": nodes_explored,
            "max_queue_size": max_queue_size,
            "time_taken": end_time - start_time
        }
    return None

random_board, empty_position = create_random_puzzle()
print("Random Initial Board:")
for row in random_board:
    print(row)

solution = solve_puzzle(random_board)
if solution:
    print(f"\nSteps to solve: {solution['steps']}")
    print(f"Nodes explored: {solution['nodes_explored']}")
    print(f"Max queue size: {solution['max_queue_size']}")
    print(f"Time taken: {solution['time_taken']} seconds")
else:
    print("No solution found.")
