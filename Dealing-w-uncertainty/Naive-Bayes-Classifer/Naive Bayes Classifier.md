# The Naive Bayes Classifier
The Naive bayes classifier is a useful application of [[Bayes Rule]]. It is a machine learning technique that can be used to classify objects such as text documents into two or more classes. The classifier is trained by analyzing a set of training data for which the correct classes are given.

Focusing on how to use the bayes rule to calculate probability, take this example;
>      P(spam∣words)=P(words ∣ spam)P(spam)÷P(words)

This is the probability of a message being spam given the words it contains. If this probability is high, then the filter may automatically delete the message or put it into a junk mail folder.

The idea is to use a large collection of spam messages to estimate the frequency of each word in them, which can be used as P(words \ | \ spam)P(words ∣ spam). The same is done for non-spam messages, which is often called "ham", to estimate P(words \ | \ ham)P(words ∣ ham). As you may notice, the Bayes rule formula above doesn't really include the latter term, but it is needed to calculate P(words)P(words), which refers to the word frequencies in all messages (either ham or spam).

> Think of P(words | ham) as  1 - P(words | spam)

>The reason why the Naive Bayes classifier is called 'naive' has to do with processing each word in the message independently and ignoring their order. So according to the Naive Bayes model, a message with the content 'dog bit man' is no different from 'man bit dog'. This way of ignoring the word order is often called a 'bag of words' approach, and we'll return to this issue later in the course.

Processing the words independently leads to a nice procedure where the Bayes rule is applied repeatedly to update the probability each time a new word is received. The resulting algorithm is as follows:
	- start with the odds 1:1, which means that the probability of spam is 0.5,
	- calculate the so called likelihood ratio as r=P(word ∣ spam)÷P(word ∣ ham) 
	- multiply the current odds by r
	- repeat steps 2 and 3 untill all the words have been processed

To give a simple artificial example, suppose the message is just two words: 'million conferences.' We need the frequencies of the words 'million' and 'conferences' in both spam as well as ham, which can easily be estimated from a collection of both kinds of messages. Let's suppose the frequencies have been estimated as follows:

spam                            ham<br>
million            0.0016285     0.0003198<br>
conferences  0.0000100     0.0000391

The ratios calculated in step 2 of the algorithm are then (rounded to four decimal places):

> P(million ∣ spam)÷P(million ∣ ham)=0.0016285÷0.0003198=5.0923

> P(conferences ∣ spam)÷P(conferences ∣ ham)=0.0000100÷0.0000391=0.2554

When the odds 1:1 is multiplied by the first one, it becomes 5.0923:1. This means that given just the word 'million', the probability that the message is spam is about five times as high as the probability that it's ham: the message looks to be spam but may well turn out to be ham after all. With the second word 'conferences', the odds are multiplied by 0.2554 so it becomes (0.2554×5.0923):1=1.30:1. Now the chances are almost equal that the message is either spam or ham.

Recall that you can get probability values from odds by using the following simple formula:

> if odds = x:y, then probability = x÷(x+y)

