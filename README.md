# assortnet
A Python package for calculating the assortativity coefficient and the mixing matrix for weighted networks and binary networks.

Most of the functions are translated from its R version. An additional function of generating mixing matrix for categorical attributes is added.

Different from its R version, the method parameters are adjusted to support NetworkX objects, and the syntax style is also similar to NetworkX. NumPy and Pandas are used to speed up computation.

Usage examples can be found in example.py.

Useful links:

  - Algorithm: https://www.sciencedirect.com/science/article/pii/S0003347214000074
  - Original R version: https://github.com/cran/assortnet
  - Manual for the original R version: https://cran.r-project.org/web/packages/assortnet/assortnet.pdf
