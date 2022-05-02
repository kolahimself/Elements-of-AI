# Warm Up Temperature

Suppose the current solution has score S_old = 150 and a small modification  to create a new solution with score S_new = 140 is tried. In the greedy solution, this new solution wouldn't be accepted because it would mean a decrease in the score. In simulated annealing, the new solution is accepted with a certain probability as explained above.

This program modifies accept_prob function so that it returns the probability of accepting the new state using simulated annealing. The program function would take the two score values (the current and the new) and the temperature value as arguments.
