# Simulated Annealing for a 2d Optimization Problem

This script uses simulated annealing to solve a simple two-dimensional optimization problem. The code runs 50 optimization tracks in parallel (at the same time)
The probability of accepting a solution that lowers the score is given by `prob = exp(–(S_old - S_new)/T).`
