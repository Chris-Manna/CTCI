def triple_step(total_steps, step = 0):
    total_steps -= step
    
    if total_steps == 0:
        return 0

    if total_steps == 1:
        # paths: 1
        return 1

    if total_steps == 2:
        # paths: 1+1, 2
        return 1 + 1

    if total_steps == 3:
        # paths: 1+1+1, 1+2, 2+1, 3
        return 4
    
    if total_steps == 4:
        #          path(1)+path(1)+path(1)+path(1) 1
        #          path(1)+path(2) # 1
        #          path(2)+path(1) # 1
        #          path(2)+path(2) # 1
        #          path(1)+path(3) # 4
        #          path(3)+path(1) # 5

        # paths:   1+1+1+(1)
        #    
        #    (1)+1+2        ; (1)+2+1        ; 2+1+(1)        ; 2+2            ;
        #          path(1) + path(3); path(3)+path(1)
        # paths:   1+3, 3+1 steps
        return 4
    

    hop = [1, 2, 3]
    if total_steps <= 3:
        return triple_step(total_steps)
    
    skip_paths = 0
    
    skip_paths += triple_step(total_steps, hop[0])
    skip_paths += triple_step(total_steps, hop[1])
    skip_paths += triple_step(total_steps, hop[2])

    return skip_paths
