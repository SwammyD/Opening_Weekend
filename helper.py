import pickle

weights = [-0.23448971,  1.80231872,  0.68723693,  1.21857071,  0.98962106,  1.56072044,
  2.00007757,  0.16537231,  0.3793386]

pickle.dump( weights, open( "nnweights.p", "wb" ) )