# K-core Algorithm Optimization
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## Description
This work is a implementation based on 2018 IEEE paper "Scalable K-Core Decomposition for Static Graphs Using a Dynamic Graph Data Structure".
## Naive Method
## Effective Method
Previously we found all vertices with degree peel = 1, and
delete them with their incident edges from G. 

Now, however, we do not delete the vertices and edges. 
Instead, when we find a vertex u, we flag u and decrement the degree of u and all
of u’s neighbors. Vertices that are flagged are not considered
to be present in G, although they are not explicitly deleted.

## Reference

- K-Core Decomposition of Large Networks on a Single PC
 
  https://dl.acm.org/doi/pdf/10.14778/2850469.2850471
 
 
- A Distributed k-Core Decomposition Algorithm on Spark
 
  https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8258018
 
 
- Scalable K-Core Decomposition for Static Graphs Using a Dynamic Graph Data Structure
 
  https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8622056
