import json
import cPickle as pickle

def paradoxCatcher(modelfile, configFile):
    # loading config and model files
    config_list = []
    with open(configFile, 'r') as ff:
        for line in ff:
            if not line.startswith('#'):
                config_list.append(json.loads(line))
    with open(modelfile, 'rb') as fb:
        loaded_model = pickle.load(fb)
    # getting irrelevant params
    all_columns = loaded_model.keys()
    print "List of attributes in the model:\n", ', '.join(all_columns)
    params = raw_input("Please input the irrelevant parameters in the dataset separated by a comma or press "
                                  "Enter to continue:")
    irrelevant_params = []
    if params != '':
        tmp_params = params.split(',')
        for param in tmp_params:
            param = param.strip()
            assert param in all_columns, "The parameter %s doesn't exist in the dataset." %param
            irrelevant_params.append(param)
    counter = 0
    paradox_flag = 0
    conf_idx=  0
    for param_set in config_list:
        conf_idx+=1
        print "Checking confifg %d out of %d for paradoxes: "%(conf_idx,len(config_list))
        for param1 in param_set.keys() :
            if param1 in loaded_model.keys():
                for param2 in param_set.keys():
                    if param2 in loaded_model.keys():
                        if param1 != param2 and param1 not in irrelevant_params and param2 not in irrelevant_params:
                            if param_set[param1] not in loaded_model[param1]:
                                counter += 1
                                continue
                            if len(loaded_model[param1][param_set[param1]][
                                       param2]) == 0:  # this means this parameter is not unique (with a freq_threshold=2)
                                continue
                            elif param_set[param2] not in loaded_model[param1][param_set[param1]][param2].keys():

                                all_keys = loaded_model[param1][param_set[param1]][param2]
                                conf_sum = sum([all_keys[xx]['__probability'] for xx in all_keys.keys()])
                                if conf_sum == 1:
                                    print "** Hard Paradox detected **"
                                else:
                                    print "Soft Paradox detected"
                                print "confidence = %f%%, instances = %d: " % (
                                    conf_sum * 100, len(loaded_model[param1][param_set[param1]][param2]))
                                print param1 + " = " + param_set[param1] + " and " + param2 + " = " + param_set[
                                    param2]
                                if conf_sum == 1:
                                    print "%s must be either of the followings: " % (param2)
                                    print [xx for xx in loaded_model[param1][param_set[param1]][param2].keys()]
                                paradox_flag = 1
                                print
        if paradox_flag == 0:
            print "\t~~~No paradox found~~~"