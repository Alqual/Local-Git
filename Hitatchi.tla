define DFS {
    1. start from node 1
    2. for every node i, find all the nodes j that are connected to i
    3. for every node j, if j is not visited, visit j and repeat step 2
    4. if all the nodes are visited, stop
}


define d(i,j) {
    1. minimum edge counts of the tree between node i and node j
    2. calculate by DFS
    3. In DFS, when the node j is child, log the edge counts between parent i and child j
    4. if log is longer than the previous log between parent i and child j, update the log
}
find [p_i,i=1,2,..,n] such that
every (i,j) in [1,n] satisfy{
if d(i,j)==3 ->  (p_i+p_j)%3== 0 or (p_i*p_j)%3 ==0 
}