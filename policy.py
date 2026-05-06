

value_function = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

gamma = 0.9

def uniform():

    global value_function

    for i in range(10):

        new_function = []
        for _ in range(5):
            new_function.append([0] * 5)

        for j in range(5):
            for k in range(5):

                #print(f"j: {j}, k: {k}")

                new_function[j][k] = get_update(j, k)

        print(f"Iteration {i+1}:")
        print_grid(new_function)
        #print(f"Difference : {value_function - new_function}")

        
        value_function = new_function
        


def get_update(j, k):

    #("up", "down", "left", "right")
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    # This accounts for state A jumping to A' 
    if j == 0 and k == 1: 
        return gamma * value_function[4][1] + 10
        
    # This accounts for state B jumping to B' 
    elif j == 0 and k == 3: 
       return gamma * value_function[2][3] + 5
        

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

        
        value += (gamma * value_function[nj][nk]) + reward

    return value / 4


def print_grid(grid):
    
    for row in grid:
        print(" ".join(f"{val:6.2f}" for val in row))

    print()


def main():

    uniform()

if __name__ == "__main__":
    main()