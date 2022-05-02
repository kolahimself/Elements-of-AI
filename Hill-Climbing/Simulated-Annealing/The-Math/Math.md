# Simulated Annealing: the math

The probability of accepting the new solution with score <i>S<u>new<u/><i/> when the current solution has score  <i>S<u>old<u/><i/> is given by the formula:
  

    prob = exp(-(S_old - S_new) ÷ T)

 where T is the temperature.
  A higher value of T makes the search essentially a random walk, wandering around with no aim to go either higher or lower. When you set the temperature to zero, the search should shoot straight up towards a nearby local optimum. Neither seems to take you to the highest peak except perhaps with a fair amount of luck.
