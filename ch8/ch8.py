class Stairs:
    def triple_step(self, total_steps):

        easy_dict = {0: 0, 1: 1, 2: 2, 3: 4}

        if total_steps <= 3:
            return easy_dict[total_steps]


        if total_steps <= 3:
            return self.triple_step(total_steps)
        return (
            self.triple_step(total_steps - 3)
            + self.triple_step(total_steps - 2)
            + self.triple_step(total_steps - 1)
        )

    # 6
    def triple_step_memo(self, total_steps, memo = [0,1,2,4]):

        if total_steps <= 3:
            return memo[total_steps]
        # 1 paths:   1
        # 2 paths:   1+1,           2
        # 3 paths:   1+1+1,         1+2, 2+1,                                                 3
        # 4 paths:   1+1+1+1,       1+1+2, 1+2+1, 2+1+1,                2+2,                  1+3, 3+1
        # 5 paths:   1+1+1+1+1,     1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 2+2+1,2+1+2, 1+2+2,   1+1+3, 1+3+1, 3+1+1,    3+2, 2+3
        # 7 paths:   1+1+1+1+1+1,   1+1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 2+2+1,2+1+2, 1+2+2,   1+1+3, 1+3+1, 3+1+1,    3+2, 2+3
        # 8 paths: 
        # 9 paths: 

        
        # [0,1,2,4]

        return (
            self.triple_step_memo(memo[total_steps - 3], memo) # self.triple_step_memo(memo[6-3], [0,1,2,4])
            + self.triple_step_memo(memo[total_steps - 2], memo)
            + self.triple_step_memo(memo[total_steps - 1], memo)
        )

def towers_of_hanoi():
    tower1 = None
    tower2 = None
    tower3 = None
    
    pass