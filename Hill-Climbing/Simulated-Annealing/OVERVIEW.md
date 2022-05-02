# Simulated annealing

One of the simplest and most effective solutions is simulated annealing. It was invented by Scott Kirkpatrick, Daniel Gelatt, and Mario P. Vecchi in 1983 taking inspiration from metallurgy, where cooling a metal object slowly allows its crystal structure to find a minimum energy configuration. The method is remarkably simple. Instead of only allowing changes that improve the solution (go uphill), some changes that make it worse (go downhill) are also allowed with some probability. The probability of allowing a downwards transition depends on two things: 
- how much downwards it goes
- a so called 'temperature.'
<br/> 
The higher the temperature, the higher the probability of allowing a downhill move. The idea is to start at a high temperature so that the changes are more or less random, but to gradually decrease the temperature so that eventually, the probability of going downwards becomes vanishingly small.
