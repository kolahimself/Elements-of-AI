import numpy as np


def generate(p1):
    # change this so that it generates 9996 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0,1], p=[1-p1, p1], size=9996)
    return seq

  
def count(seq):
    # insert code to return the number of occurrences of 11111 in the sequence
    occurence = 0
    i = 0
    while i < len(seq):
        if seq[i : i + 5].all():
            occurence +=1
        i += 1
    return occurence
  
  
def main(p1):
    seq = generate(p1)
    return count(seq)
  
# Check
if main(2/3) > 1230 and main(2/3) < 1404:
    print("Monte-Carlo Method Check Completed")
    print(f'Predicted Occurence of consecutive 11111s: {main(2/3)}')
