.. ParadoxCatcher documentation master file, created by
   sphinx-quickstart on Sun Apr  1 13:35:45 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ParadoxCatcher
===============
ParadoxCatcher is a tool to generate valid configurations for spoofing to resist web tracking. This tools works in four modes, namely Model Builder, Paradox Catcher (not to be confused with the name of the tool itself), Valid Spoof Generator and Dependency finder. You can get the help using the -h flag: 


.. code-block:: bash 

	$ ../main.py -h
	usage: main.py [-h]
		       (-m sqlDB uthreshold filename | -c modelfile configfile | -s modelfile dthreshold | -d modelfile attribute value dthreshold)

	ParadoxCatcher: a tool for generting valid browser configuration for spoofing
	to resist web tracking.

	optional arguments:
	  -h, --help            show this help message and exit

	  -m sqlDB uthreshold filename, --model sqlDB uthreshold filename
				Generate the model file (filename) using the my
				database (sqlDB) and Uniqueness Threshold (uthreshold)
	  -c modelfile configfile, --catcher modelfile configfile
				Reveals the paradoxes in a set of configuration stored
				in a configfile in json format, based on the model in
				modelfile .
	  -s modelfile dthreshold, --spoofgenerator modelfile dthreshold
				Generates a random set of attributes/values to be
				spoofed without causing a paradox.
	  -d modelfile attribute value dthreshold, --dependency modelfile attribute value dthreshold
				Finding the dependencies of a target attirbute/value
				to prevent paradoxes

Each of the modes and corresponding usage and examples are discussed and presented in the following sections: 

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modelbuilder
   paradoxcatcher
   validspoofgenerator
   dependencyfinder

.. Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
