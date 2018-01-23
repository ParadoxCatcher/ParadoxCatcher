import cPickle as pickle
import random
import numpy as np
import dependencyFinder

def spoofgenerator(modelfile, dthreshold):
    with open(modelfile, 'rb') as fb:
        model_data = pickle.load(fb)
    param_to_change = random.choice([kk for kk in model_data.keys()])
    values_probs_tup = [(kk, model_data[param_to_change][kk]['__probability']) for kk in model_data[param_to_change].keys()]
    probs = [pp[1] for pp in values_probs_tup]
    values = [pp[0] for pp in values_probs_tup]
    param_value = values[probs.index(max(probs))]
    return dependencyFinder.dependencyFinder(modelfile,param_to_change,param_value,dthreshold)