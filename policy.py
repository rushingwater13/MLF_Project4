
rewards = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0],
    [0, 0, 0, 0, 0],
    [0, 10, 0, 0, 0],
]

policy = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


def uniform():
    new_policy = []
    for i in range(6):
        new_policy.append([])

    for i in range(11):
        for j in len(policy):
            for k in len(policy[j]):

                new_value = 0.25 * update(j, k)
                new_policy[j].append(new_value)


        policy = new_policy
        print(f"Iteration {i+1}: {policy}")


def update(j, k):

    #("up", "down", "left", "right")
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    value = 0;
    for h, w in directions:
        if j + h < 0:
            h += 1
        elif j + h > 4:
            h -= 1

        if k + w < 0:
            w += 1
        elif k + w > 4:
            w -= 1
        
        value += policy[j + h][k + w] + rewards[j + h][k + w]

    return value



uniform()