Valid Spoof Generator
=====================

In this defensive mode, this tool makes a suggestion for a set of attributes and corresponding values, which if spoofed, will not be paradoxical. The suggested configuration can be used by a front-end or browser extension that spoofs browser attributes on each session. 

Example usage and output:

.. code-block:: bash 

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
