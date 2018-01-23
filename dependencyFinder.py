import cPickle as pickle


def dependencyFinder(modelfile, attribute, value, dthreshold):
    with open(modelfile, 'rb') as fb:
        model_data = pickle.load(fb)
    # getting irrelevant params
    all_columns = model_data.keys()
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
    # finding dependencies recursively
    dependentparams = recursive_depFinder(model_data,attribute,value,dthreshold,irrelevant_params)
    return dependentparams

def recursive_depFinder(model_data, attribute,value,dthreshold,irrelevant_params, current_set =[], iteration = 1):
    current_keys = [elem[0] for elem in current_set]
    must_change_parameters = [(attribute, value)]
    for key in model_data[attribute][value].keys():
        # if key not in current_keys:
        if key not in ['__probability'] + irrelevant_params:
            next_values = [(possible_val, model_data[attribute][value][key][possible_val]['__probability']) for possible_val in
                           model_data[attribute][value][key]]
            try:
                max_prob = max([ii[1] for ii in next_values])
            except ValueError:
                continue
            value_of_max_prob = [ii[0] for ii in next_values if ii[1] == max_prob][0]
            if max_prob > dthreshold:
                if key in current_keys:
                    if value_of_max_prob != current_set[current_keys.index(key)][1]:
                        print "WARNING: PARADOX FOUND!"
                        return
                else:
                    if iteration > 1:
                        print "Indirect parameter: %s -> %s -> %s"%(attribute, key, value_of_max_prob)
                    else:
                        print "Direct parameter: %s -> %s"%(key,value_of_max_prob)
                    must_change_parameters.append((key,value_of_max_prob))
    must_change_parameters_cpy = must_change_parameters[:]
    for param in must_change_parameters_cpy[1:]:
        if iteration>1:
            indirect_values = recursive_depFinder(model_data,param[0],param[1],dthreshold,irrelevant_params,current_set=current_set + must_change_parameters[1:],iteration=iteration+1)
        else:
            indirect_values = recursive_depFinder(model_data,param[0], param[1],dthreshold,irrelevant_params,current_set=must_change_parameters,iteration=iteration + 1)
        must_change_parameters += indirect_values
    if iteration > 1 :
        return must_change_parameters[1:]
    else:
        return must_change_parameters
