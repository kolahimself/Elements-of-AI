# Simulated Annealing: the math

The probability of accepting the new solution with score <i>S<u>new<u/><i/> when the current solution has score  <i>S<u>old<u/><i/> is given by the formula:
  

    prob = exp(-(S_old - S_new) ÷ T)

 where T is the temperature.
