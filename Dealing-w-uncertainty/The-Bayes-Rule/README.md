# Bayes Rule

Instead of using conditional probability to make inferences about something we don't know based on a specific piece of information, e.g (previous example) what we didn't know was the nationality of the lottery winner and the piece of information that we made use of was the fact that the winner was a fisher.

There is a specific way to calculate such conditional probabilities that is particularly useful in many applications, namely the Bayes rule. The often-used formula for the Bayes rule is:

> $P(A ∣ B) = P(B ∣ A) P(A) \over P(B)$

using specific A or B examples:
> P(Denmark ∣ fisher)=P(fisher ∣ Denmark) P(Denmark)÷P(fisher)

*P(Denmark∣fisher) stands for the probability of a person being Danish, given that they are a fisher. To calculate it, we now need numerical values for the three quantities on the right, namelyP(fisher \mid Denmark)P(fisher∣Denmark), P(Denmark)P(Denmark) and P(fisher)P(fisher).*

P(Denmark∣fisher) stands for the probability of a person being Danish, given that they are a fisher. To calculate it, we now need numerical values for the three quantities on the right, namelyP(fisher \mid Denmark)P(fisher∣Denmark), P(Denmark)P(Denmark) and P(fisher)P(fisher).

The first term is the probability that a random person is a fisher given that they live in Denmark. This we calculated in the previous section to be about 0.034\%0.034%. The second term is the probability that a random person lives in Denmark, considering the Nordic countries only at this time, which we also have already calculated and found to be about 21.5\%21.5%.

The third and the last term that we need is the one that may sometimes require a bit of work to figure out. Here, it is quite straightforward to calculate by adding up the number of fishers in all five countries, which gives 21{,}71121,711, and dividing this by the total population of the said countries, 26{,}067{,}00026,067,000. This too we have already calculated and it can be found in the first table of the previous section: about 0.083\%0.083%.

For the calculations, we'll write the probabilities as plain decimal numbers instead of percentages (just divide each percentage by 100100). So here's the formula with the above numbers substituted in the correct places:

> P(Denmark ∣ fisher)=0.00034×0.215÷0.00083=0.088

(rounded to three decimal places), or about 8.8\%8.8%. Recall that we already knew the result since we had calculated it without the Bayes rule above. (If you have an eye for details, you may have noticed that we actually got the result 8.7\%8.7% earlier. This is caused by rounding errors – had we used a more accurate value for the proportion of fishers in Denmark than 0.000340.00034, we would have gotten the same result, 8.7\%8.7%, also here. This illustrates the importance of using a sufficient number of digits especially for small numbers. With computers, it's much easier to maintain high precision since we don't have to actually write down the numbers, although there are cases where floating point rounding errors become problematic as well.)

The good news is that we got the right result, but you are probably wondering why on Earth we went to the trouble of using the Bayes rule since there was a direct way to reach the same result? The answer is that we wanted to illustrate the use of the Bayes rule so that we could use it later in other cases. It is often the case that we know the three terms on the right side of the Bayes rule but we don't know the terms required for the direct calculation. Typical cases like this include medical diagnosis (see for instance the breast cancer screening example in the Introduction to AI) and other scenarios where we know the probability of the effect (test result) given its cause (a medical condition), but not the other way around.
