# Greedy Solutions

## Example - Reach The Highest Summit

Let the elevation at each point on the mountain be stored in array h of size 100. The elevation at the leftmost point is thus stored in h[0] and the elevation at the rightmost point is stored in h[99].

Here's an example chart. The green box represents Venla's starting position, and the red triangle marks the point where Venla stops. A blue triangle (not shown here) marks the summit.![1 3-Exercise_3-Reaching_the_highest_summit](https://user-images.githubusercontent.com/73860607/166169166-c1e83013-1f24-4c48-af0f-dbfdd7957de9.svg)

![image](https://user-images.githubusercontent.com/73860607/166169176-37a5ac39-7c69-4385-b116-2cac1f1b9bec.png)

This program starts at a random position on the mountain and keeps going to the right until it can no longer go up. However, perhaps the mountain is a bit rugged which means it's necessary to look a bit further ahead.



- The simple hill climbing solution where we only go upwards is often said to be a greedy method: it greedily optimizes the short term gain and refuses to incur some temporary loss even if it would lead to better long-term gain.
