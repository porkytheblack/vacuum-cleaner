

# - # is wall
# - . is clean
# - D is Dirty

def display(room: list[list[str]], covered: list[list[int]]):
    for cell in covered:
        room[cell[1]][cell[0]] = '✅'
    for line in room:
        print(', '.join(map(str, line)))

def check_for_dirt(environment: list[list[str]]):
    dirt_found :bool = False

    for row in environment:
        for cell in row:
            if cell == "D":
                dirt_found = True
                break
            else:
                continue

    return dirt_found

def find_in_path(cell: list[int], path: list[list[int]]):
    found = False
    for _cell in path:
        if _cell[0] == cell[0] and _cell[1] == cell[1]:
            found = True
            break
        else:
            continue
    return found

def next_direction(environment: list[list[str]], previous_path: list[list[int]]):
    current_location = previous_path[-1]

    move_up = [
        current_location[0],
        current_location[1] - 1,
    ]

    already_moved_up = find_in_path(move_up, previous_path)

    is_up_wall = environment[move_up[1]][move_up[0]] == "#"

    if not already_moved_up and not is_up_wall:
        print("⏫")
        return move_up

    move_right = [
        current_location[0] + 1,
        current_location[1],
    ]

    already_moved_right = find_in_path(move_right, previous_path)

    is_right_wall = environment[move_right[1]][move_right[0]] == "#"

    if not already_moved_right and not is_right_wall:
        print("⏩")
        return move_right


    move_down = [
        current_location[0],
        current_location[1] + 1,
    ]

    already_moved_down = find_in_path(move_down, previous_path)

    is_down_wall = environment[move_down[1]][move_down[0]] == "#"

    if not already_moved_down and not is_down_wall:
        print("⏬")
        return move_down

    move_left = [
        current_location[0] - 1,
        current_location[1],
    ]

    already_moved_left = find_in_path(move_left, previous_path)

    is_left_wall = environment[move_left[1]][move_left[0]] == "#"

    if not already_moved_left and not is_left_wall:
        print("⏪")
        return move_left





# General direction TopRightDownLeft
def agent(environment: list[list[str]], path: list[list[int]], energy_consumed: int):
    dirt_found = check_for_dirt(environment)

    if not dirt_found and len(path) == 64:
        return environment

    next_cell = next_direction(environment, path)
    path.append(next_cell)
    if next_cell[1] is not None:
        if environment[next_cell[1]] is not None:
            if  environment[next_cell[1]][next_cell[0]] == "D":
                environment[next_cell[1]][next_cell[0]] = "."
                energy_consumed = energy_consumed + 2
            else:
                energy_consumed = energy_consumed + 1

    print("Current Environment:")
    display(environment, path)
    print("TOTAL ENERGY CONSUMED:", energy_consumed)

    return agent(environment, path, energy_consumed)
