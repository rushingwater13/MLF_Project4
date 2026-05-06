

value_function = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

gamma = 0.9

def calculate_function(mode):

    global value_function

    for i in range(10):

        new_function = [[0] * 5 for _ in range(5)]
        diff = [[0] * 5 for _ in range(5)]

        for j in range(5):
            for k in range(5):

                new_function[j][k] = get_update(j, k, mode)
                diff[j][k] = new_function[j][k] - value_function[j][k]

        print(f"Iteration {i+1}:")
        print_grid(new_function)

        print(f"Difference (new - old):")
        print_grid(diff)

        
        value_function = new_function
        


def get_update(j, k, mode):

    #("up", "down", "left", "right")
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    if mode == "B6":
        B_reward = 6
    elif mode == "B7":
        B_reward = 7
    else:
        B_reward = 5



    # This accounts for state A jumping to A' 
    if j == 0 and k == 1: 
        return gamma * value_function[4][1] + 10
        
    # This accounts for state B jumping to B' 
    elif j == 0 and k == 3: 
       return gamma * value_function[2][3] + B_reward
        
    best_value = float('-inf')
    value = 0;

    # This is everyone else, accounting for walls
    for h, w in directions:  

        nj = j + h
        nk = k + w 

        if nj < 0 or nj > 4 or nk < 0 or nk > 4:
            nj = j
            nk = k
            reward = -1
        else:
            reward = 0

        candidate = (gamma * value_function[nj][nk]) + reward
        value += candidate
        best_value = max(best_value, candidate)


    if mode == "Uniform":
        return value / 4
    else:
        return best_value


def print_grid(grid):
    
    for row in grid:
        print(" ".join(f"{val:6.2f}" for val in row))

    print()


def reset_function():
    return [[0] * 5 for _ in range(5)]


def main():

    global value_function

    policies = ["Uniform", "Optimal", "B6", "B7"]

    for policy in policies:
        value_function = reset_function()
        print(f"-------- {policy} --------")
        calculate_function(policy)

if __name__ == "__main__":
    main()