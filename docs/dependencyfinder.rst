Dependency Finder
==================

Several browser addons, such as User-Agent Switcher, attempt to spoof an attribute of the browser in order to defend against browser fingerprinting. As mentioned previously, a blind approach to this easily causes a paradox in the browser configuration. In dependency finder mode, the tool informs the user about the dependencies of an attribute and suggests values for them. To prevent a paradox, besides the target attribute, its dependents should be changed as well. 

Example usage and output: 

.. code-block:: bash 

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
