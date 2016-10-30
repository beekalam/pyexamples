try:
    import cPickle as pickle
except:
    import pickle

import pprint

data = [{'a': 'A', 'b': 2, 'c': 3.0}]

print 'DATA:'
#pprint.pprint(data)
print data

data_string = pickle.dumps(data)
print data_string
