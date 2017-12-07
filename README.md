The approach I would apply is: 
- Break down entry in pieces that the mentioned method rank_trips() supports (up to 5) 
- Then Build a (heap-like) tree and rearrange the nodes and combine the subtrees with new calls to the original rank_trips() method 

O(n log(n))