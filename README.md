# ParadoxCatcher

ParadoxCatcher is a tool to generate valid configurations for spoofing to resist web tracking. This tools works in four modes:

```
$ ./main.py -h

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
```




**Model Builder**

The model builder is a preprocessing stage that identifies sources of technical inconsistencies 
and provides stochastic information about distribution of various configurations. As the name 
implies, this tool builds the model file based on the pseudocode provided in Listing 1. To build 
the model, Model Builder takes as input a dataset of web fingerprints as well as a Uniqueness 
Threshold, builds the model and saves it as a cPickle file. This file is later used in the other 
modes make an inference based on the input. Example: 

```
$ ./main.py -m fingerprint 100 ./model_files/extracted_data_freq100.pickle

Username: root
Password: 
List of attributes in the dataset:
counter, id, addressHttp, time, userAgentHttp, acceptHttp, hostHttp, connectionHttp, encodingHttp, languageHttp, orderHttp, pluginsJS, platformJS, cookiesJS, dntJS, timezoneJS, resolutionJS, localJS, sessionJS, IEDataJS, canvasJS, webGLJs, fontsFlash, resolutionFlash, languageFlash, platformFlash, adBlock, vendorWebGLJS, rendererWebGLJS, octaneScore, sunspiderTime, pluginsJSHashed, canvasJSHashed, webGLJsHashed, fontsFlashHashed
Please input the irrelevant parameters in the dataset separated by a comma or press Enter to continue:octaneScore, sunspiderTime, timezoneJS, id, counter, time
5.000000% of columns are done...
11.000000% of columns are done...
14.000000% of columns are done...
17.000000% of columns are done...
20.000000% of columns are done...
22.000000% of columns are done...
25.000000% of columns are done...
28.000000% of columns are done...
31.000000% of columns are done...
34.000000% of columns are done...
37.000000% of columns are done...
40.000000% of columns are done...
45.000000% of columns are done...
48.000000% of columns are done...
51.000000% of columns are done...
54.000000% of columns are done...
57.000000% of columns are done...
60.000000% of columns are done...
62.000000% of columns are done...
65.000000% of columns are done...
68.000000% of columns are done...
71.000000% of columns are done...
74.000000% of columns are done...
77.000000% of columns are done...
80.000000% of columns are done...
88.000000% of columns are done...
91.000000% of columns are done...
94.000000% of columns are done...
97.000000% of columns are done...
Model with uniqueness threshold of 100 was built in 50 seconds.
```
 
**Paradox Catcher**

In this mode, a browser configuration, i.e. set of attributes, is provided as input to the tool, 
and the output will reveal paradoxical attributes in the following format:

*Paradox_type (confidence, number_of_instances)
source_attribute=source_attribute_value
target_attribute=target_attribute_value* 

In the case of a hard paradox, the possible non-paradoxical values will be output as well. The 
lookup order to produce the output in the model is as follows: source attribute, source attribute 
value, target attribute, target value and its probability. In the case that a source or target 
attribute is not included in the model, the tool disregards that attribute.  Such an occurrence 
is highly likely a weakness in the statistical model due to either a Uniqueness Threshold that 
is too high, or an original dataset that is too small.  To do otherwise would induce artificial 
changes in the possibility of a paradox occurring or not. Example: 

```
$ ./main.py -c ./model_files/extracted_data_freq1.pickle test_config.txt

List of attributes in the model:
acceptHttp, cookiesJS, languageHttp, fontsFlashHashed, platformFlash, userAgentHttp, orderHttp, addressHttp, connectionHttp, resolutionJS, canvasJS, fontsFlash, languageFlash, adBlock, pluginsJS, sessionJS, vendorWebGLJS, dntJS, encodingHttp, resolutionFlash, IEDataJS, webGLJs, hostHttp, canvasJSHashed, webGLJsHashed, rendererWebGLJS, localJS, platformJS, pluginsJSHashed
Please input the irrelevant parameters in the dataset separated by a comma or press Enter to continue:
Checking confifg 1 out of 1 for paradoxes: 
** Hard Paradox detected **
confidence = 100.000000%, instances = 1: 
addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1 and platformJS = iPad
platformJS must be either of the followings: 
[u'Linux armv7l']

** Hard Paradox detected **
confidence = 100.000000%, instances = 4: 
resolutionJS = 360x640x32 and platformJS = iPad
platformJS must be either of the followings: 
[u'Linux aarch64', u'Linux armv8l', u'Linux armv7l', u'Linux x86_64']

** Hard Paradox detected **
confidence = 100.000000%, instances = 4: 
canvasJS =  and platformJS = iPad
platformJS must be either of the followings: 
[u'Win32', u'Linux armv8l', u'Linux armv7l', u'MacIntel']

** Hard Paradox detected **
confidence = 100.000000%, instances = 1: 
userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36 and platformJS = iPad
platformJS must be either of the followings: 
[u'Linux armv7l']

** Hard Paradox detected **
confidence = 100.000000%, instances = 4: 
canvasJSHashed = da39a3ee5e6b4b0d3255bfef95601890afd80709 and platformJS = iPad
platformJS must be either of the followings: 
[u'Win32', u'Linux armv8l', u'Linux armv7l', u'MacIntel']

Soft Paradox detected
confidence = 100.000000%, instances = 126: 
platformJS = iPad and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

** Hard Paradox detected **
confidence = 100.000000%, instances = 7: 
platformJS = iPad and resolutionJS = 360x640x32
resolutionJS must be either of the followings: 
[u'1024x1366x32', u'800x600x24', u'1024x600x32', u'768x1024x32', u'1920x1080x24', u'1024x768x24', u'1000x600x24']

Soft Paradox detected
confidence = 100.000000%, instances = 38: 
platformJS = iPad and canvasJS = 

Soft Paradox detected
confidence = 100.000000%, instances = 45: 
platformJS = iPad and userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36

Soft Paradox detected
confidence = 100.000000%, instances = 38: 
platformJS = iPad and canvasJSHashed = da39a3ee5e6b4b0d3255bfef95601890afd80709
```


**Valid Spoof Generator**


In this defensive mode, this tool makes a suggestion for a set of attributes and corresponding 
values, which if spoofed, will not be paradoxical. The suggested configuration can be used by 
a front-end or browser extension that spoofs browser attributes on each session. Example: 

```
$ ./main.py -s ./model_files/extracted_data_freq30.pickle 0.85

List of attributes in the model:
acceptHttp, cookiesJS, languageHttp, fontsFlashHashed, platformFlash, userAgentHttp, orderHttp, IEDataJS, connectionHttp, resolutionJS, canvasJS, fontsFlash, languageFlash, adBlock, pluginsJS, sessionJS, vendorWebGLJS, dntJS, encodingHttp, resolutionFlash, addressHttp, webGLJs, hostHttp, canvasJSHashed, webGLJsHashed, rendererWebGLJS, localJS, platformJS, pluginsJSHashed
Please input the irrelevant parameters in the dataset separated by a comma or press Enter to continue:
Direct parameter: cookiesJS -> yes
Direct parameter: IEDataJS -> no
Direct parameter: connectionHttp -> close
Direct parameter: sessionJS -> yes
Direct parameter: hostHttp -> amiunique-backend
Direct parameter: localJS -> yes

```

**Dependency Finder** 

Several browser addons, such as User-Agent Switcher, attempt to spoof an attribute of the browser 
in order to defend against browser fingerprinting. As mentioned previously, a blind approach to 
this easily causes a paradox in the browser configuration. In dependency finder mode, the tool 
informs the user about the dependencies of an attribute and suggests values for them.  To prevent 
a paradox, besides the target attribute, its dependents should be changed as well. Example:    

```
$ ./main.py -d ./model_files/extracted_data_freq30.pickle platformJS iPad 0.85

List of attributes in the model:
acceptHttp, cookiesJS, languageHttp, fontsFlashHashed, platformFlash, userAgentHttp, orderHttp, IEDataJS, connectionHttp, resolutionJS, canvasJS, fontsFlash, languageFlash, adBlock, pluginsJS, sessionJS, vendorWebGLJS, dntJS, encodingHttp, resolutionFlash, addressHttp, webGLJs, hostHttp, canvasJSHashed, webGLJsHashed, rendererWebGLJS, localJS, platformJS, pluginsJSHashed
Please input the irrelevant parameters in the dataset separated by a comma or press Enter to continue:
Direct parameter: acceptHttp -> text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Direct parameter: cookiesJS -> yes
Direct parameter: fontsFlashHashed -> ce30cd74ffc46157d73983a8599d5ed2d2564260
Direct parameter: platformFlash -> Flash not detected
Direct parameter: IEDataJS -> no
Direct parameter: connectionHttp -> close
Direct parameter: resolutionJS -> 768x1024x32
Direct parameter: fontsFlash -> Flash not detected
Direct parameter: languageFlash -> Flash not detected
Direct parameter: adBlock -> no
Direct parameter: pluginsJS -> 
Direct parameter: encodingHttp -> gzip, deflate
Direct parameter: resolutionFlash -> Flash not detected
Direct parameter: hostHttp -> amiunique-backend
Direct parameter: pluginsJSHashed -> da39a3ee5e6b4b0d3255bfef95601890afd80709
Indirect parameter: cookiesJS -> sessionJS -> yes
Indirect parameter: cookiesJS -> localJS -> yes
```