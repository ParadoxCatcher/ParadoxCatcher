#!/usr/bin/env python2
import argparse
import modelBuilder
import paradoxCatcher
import dependencyFinder
import validSpoofGenerator

parser=argparse.ArgumentParser(
    description='''ParadoxCatcher: a tool for generting valid browser configuration for spoofing to resist web tracking.''',
    epilog="""All's well that ends well.""")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-m','--model',nargs=3,metavar=('sqlDB', 'uthreshold','filename'),help='Generate the model file (filename) '
                                                    'using the my database (sqlDB) and Uniqueness Threshold (uthreshold)')
group.add_argument('-c','--catcher',nargs=2,metavar=('modelfile', 'configfile'),
                   help ='Reveals the paradoxes in a set of configuration stored in a configfile in json format, '
                         'based on the model in modelfile .')
group.add_argument('-s','--spoofgenerator',nargs=2,metavar=('modelfile', 'dthreshold'),help='Generates a random set of attributes/values to be'
                                                                         ' spoofed without causing a paradox.')
group.add_argument('-d','--dependency',nargs=4,metavar=('modelfile', 'attribute','value','dthreshold'), help ='Finding the dependencies of a target attirbute/value '
                                                                        ' to prevent paradoxes')
args=parser.parse_args()

if args.model:
    sql_db = args.model[0]
    uthreshold = int(args.model[1])
    filename = args.model[2]
    modelBuilder.modelBuilder(sql_db, uthreshold, filename)
elif args.catcher:
    modelfile = args.catcher[0]
    configfile = args.catcher[1]
    paradoxCatcher.paradoxCatcher(modelfile,configfile)
elif args.spoofgenerator:
    modelfile = args.spoofgenerator[0]
    dthreshold = float(args.spoofgenerator[1])
    validSpoofGenerator.spoofgenerator(modelfile,dthreshold)
elif args.dependency:
    modelfile = args.dependency[0]
    attribute = args.dependency[1]
    value = args.dependency[2]
    dthreshold = float(args.dependency[3])
    dependencyFinder.dependencyFinder(modelfile,attribute,value,dthreshold)
