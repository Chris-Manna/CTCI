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

        return (
            self.triple_step_memo(memo[total_steps - 3], memo) #self.triple_step_memo(memo[6-3], [0,1,2,4])
            + self.triple_step_memo(memo[total_steps - 2], memo)
            + self.triple_step_memo(memo[total_steps - 1], memo)
        )
