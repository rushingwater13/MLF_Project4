import matplotlib.pyplot as plt

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

    mode = mode.lower()

    for i in range(10):

        new_function = [[0] * 5 for _ in range(5)]
        diff = [[0] * 5 for _ in range(5)]

        for j in range(5):
            for k in range(5):
                new_function[j][k] = get_update(j, k, mode)
                diff[j][k] = new_function[j][k] - value_function[j][k]


        #print(f"Iteration {i+1}:")
        #print_grid(new_function)
        plot_grid(new_function, f"{mode} Iteration {i+1}", mode, f"{mode}_{i}")

        #print(f"Difference (new - old):")
        #print_grid(diff)
        plot_grid(diff, f"{mode} Difference (new-old) {i+1}", mode, f"{mode}_{i}_diff")

        
        value_function = new_function

    return value_function
        


def get_update(j, k, mode):

    #("up", "down", "left", "right")
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    if mode == "b6":
        B_reward = 6
    elif mode == "b7":
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
        
        if mode == "uniform":
            value += candidate
        else:
            best_value = max(best_value, candidate)


    if mode == "uniform":
        return value / 4
    else:
        return best_value
    

def sub_grid(grid1, grid2):
    diff = [[0] * 5 for _ in range(5)]

    for j in range(5):
        for k in range(5):
            diff[j][k] = grid1[j][k] - grid2[j][k]

    return diff



def print_grid(grid):
    
    for row in grid:
        print(" ".join(f"{val:6.2f}" for val in row))

    print()


def reset_function():
    return [[0] * 5 for _ in range(5)]


def plot_grid(grid, title, folder, file):

    plt.figure()
    plt.imshow(grid)
    plt.colorbar()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            plt.text(j, i, f"{grid[i][j]:.2f}", 
                     ha="center", va="center", color="black")
            
    plt.title(title)
    plt.xticks([])
    plt.yticks([])
    plt.savefig(f"{folder}/{file}.png")
    plt.close()



def main():

    global value_function

    policies = ["Uniform", "Optimal", "B6", "B7"]

    results = {}

    for policy in policies:
        value_function = reset_function()
        print(f"-------- {policy} --------")
        results[policy] = calculate_function(policy)

    #print("Final Difference (Optimal - Uniform)")
    sub = sub_grid(results["Optimal"], results["Uniform"])
    #print_grid(sub)
    plot_grid(sub, "Final Difference (Optimal - Uniform)", "uniform", "uni_opt_diff")


if __name__ == "__main__":
    main()