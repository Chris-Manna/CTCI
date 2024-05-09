def triple_step(total_steps, step=0, paths=0):

    easy_dict = {0: 0, 1: 1, 2: 2, 3: 4}
    total_steps -= step

    if total_steps <= 3:
        return easy_dict[total_steps]


    if total_steps <= 3:
        return triple_step(total_steps)
    return (
        triple_step(total_steps - 3)
        + triple_step(total_steps - 2)
        + triple_step(total_steps - 1)
    )
