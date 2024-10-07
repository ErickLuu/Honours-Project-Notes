### IDEAS FOR BOUNDED TREEWIDTH OF PLANAR GRAPHS

1. Use Robert's theorem on treewidth to decompose graphs into clique sum trees with cliques of size at most 3
2. Components of trees are 4 connected thus they are Hamiltonian-connected
3. If clique is of size 1 then ok
4. If clique is of size 2 then clique are vertices vw. find hamiltonian path beginning at w and ending at v, P. then the ordering v < w < P where P is the ordering of the path is also a hamiltonian connected path so number pages is 2.
5. if clique of size 3, clique uvw, then find hamiltonian path uv and have ordering u < v < P .. < w < P is also hamiltonian path. let uv be neighbours of w. we can move w to the end and add extra page for vertices out of w... so now need 3 pages but satisfies Robert's 2nd condition. 