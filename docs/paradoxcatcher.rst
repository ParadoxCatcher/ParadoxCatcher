Paradox Catcher
=================

In this mode, a browser configuration, i.e. set of attributes, is provided as input to the tool, and the output will reveal paradoxical attributes in the following format:

`Paradox_type (confidence, number_of_instances) source_attribute=source_attribute_value target_attribute=target_attribute_value`

In the case of a hard paradox, the possible non-paradoxical values will be output as well. The lookup order to produce the output in the model is as follows: source attribute, source attribute value, target attribute, target value and its probability. In the case that a source or target attribute is not included in the model, the tool disregards that attribute. Such an occurrence is highly likely a weakness in the statistical model due to either a Uniqueness Threshold that is too high, or an original dataset that is too small. To do otherwise would induce artificial changes in the possibility of a paradox occurring or not. 

Example usage and output:

.. code-block:: bash 

	$ ./main.py -c ./model_files/extracted_data_freq1.pickle test_config.txt

	List of attributes in the model:
	acceptHttp, cookiesJS, languageHttp, fontsFlashHashed, platformFlash, id, orderHttp, IEDataJS, connectionHttp, resolutionJS, canvasJS, fontsFlash, languageFlash, sunspiderTime, adBlock, timezoneJS, pluginsJS, sessionJS, vendorWebGLJS, dntJS, userAgentHttp, encodingHttp, resolutionFlash, addressHttp, webGLJs, octaneScore, hostHttp, canvasJSHashed, webGLJsHashed, rendererWebGLJS, localJS, platformJS, pluginsJSHashed
	Please input the irrelevant parameters in the dataset separated by a comma or press Enter to continue:
	Checking confifg 1 out of 1 for paradoxes: 
	Soft Paradox detected
	confidence = 17.349218%, instances = 154: 
	acceptHttp = text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8 and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 29.456441%, instances = 378: 
	acceptHttp = text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8 and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 11.041158%, instances = 306: 
	cookiesJS = yes and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 34.327536%, instances = 828: 
	cookiesJS = yes and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 24.561404%, instances = 73: 
	languageHttp = en-US,en;q=0.8 and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 32.631579%, instances = 169: 
	languageHttp = en-US,en;q=0.8 and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 81.508772%, instances = 168: 
	languageHttp = en-US,en;q=0.8 and userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36

	Soft Paradox detected
	confidence = 99.719298%, instances = 12: 
	languageHttp = en-US,en;q=0.8 and platformJS = iPad

	Soft Paradox detected
	confidence = 13.683413%, instances = 135: 
	fontsFlashHashed = ce30cd74ffc46157d73983a8599d5ed2d2564260 and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 31.961626%, instances = 493: 
	fontsFlashHashed = ce30cd74ffc46157d73983a8599d5ed2d2564260 and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 13.683413%, instances = 135: 
	platformFlash = Flash not detected and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 31.961626%, instances = 493: 
	platformFlash = Flash not detected and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 3.381764%, instances = 1: 
	orderHttp = Upgrade-Insecure-Requests Referer Connection Accept X-Real-IP Accept-Language Accept-Encoding User-Agent Host and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 13.577154%, instances = 119: 
	orderHttp = Upgrade-Insecure-Requests Referer Connection Accept X-Real-IP Accept-Language Accept-Encoding User-Agent Host and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 99.724449%, instances = 11: 
	orderHttp = Upgrade-Insecure-Requests Referer Connection Accept X-Real-IP Accept-Language Accept-Encoding User-Agent Host and platformJS = iPad

	Soft Paradox detected
	confidence = 29.881040%, instances = 338: 
	connectionHttp = close and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 45.603385%, instances = 1223: 
	connectionHttp = close and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 3.016241%, instances = 3: 
	resolutionJS = 360x640x32 and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 1.392111%, instances = 2: 
	resolutionJS = 360x640x32 and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 99.535963%, instances = 3: 
	resolutionJS = 360x640x32 and platformJS = iPad

	Soft Paradox detected
	confidence = 13.043478%, instances = 2: 
	canvasJS =  and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 52.173913%, instances = 4: 
	canvasJS =  and userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36

	** Hard Paradox detected **
	confidence = 100.000000%, instances = 4: 
	canvasJS =  and platformJS = iPad
	platformJS must be either of the followings: 
	[u'Win32', u'Linux armv8l', u'Linux armv7l', u'MacIntel']

	Soft Paradox detected
	confidence = 13.683413%, instances = 135: 
	fontsFlash = Flash not detected and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 31.961626%, instances = 493: 
	fontsFlash = Flash not detected and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 13.683413%, instances = 135: 
	languageFlash = Flash not detected and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 31.961626%, instances = 493: 
	languageFlash = Flash not detected and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 83.333333%, instances = 1: 
	userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36 and canvasJS = 

	Soft Paradox detected
	confidence = 83.333333%, instances = 1: 
	userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36 and adBlock = yes

	Soft Paradox detected
	confidence = 83.333333%, instances = 1: 
	userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36 and vendorWebGLJS = Not supported

	Soft Paradox detected
	confidence = 83.333333%, instances = 1: 
	userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36 and webGLJs = Not supported

	Soft Paradox detected
	confidence = 83.333333%, instances = 1: 
	userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36 and canvasJSHashed = da39a3ee5e6b4b0d3255bfef95601890afd80709

	Soft Paradox detected
	confidence = 83.333333%, instances = 1: 
	userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36 and webGLJsHashed = 8e635455c1c04acc72cc3cb8b3930fa2002922c7

	Soft Paradox detected
	confidence = 83.333333%, instances = 1: 
	userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36 and rendererWebGLJS = Not supported

	** Hard Paradox detected **
	confidence = 100.000000%, instances = 1: 
	userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36 and platformJS = iPad
	platformJS must be either of the followings: 
	[u'Linux armv7l']

	Soft Paradox detected
	confidence = 15.089188%, instances = 132: 
	adBlock = yes and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 30.123771%, instances = 307: 
	adBlock = yes and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 86.548963%, instances = 262: 
	adBlock = yes and userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36

	Soft Paradox detected
	confidence = 14.551334%, instances = 46: 
	timezoneJS = -120 and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 36.580437%, instances = 172: 
	timezoneJS = -120 and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 79.506871%, instances = 147: 
	timezoneJS = -120 and userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36

	Soft Paradox detected
	confidence = 19.559734%, instances = 91: 
	pluginsJS =  and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 37.858289%, instances = 303: 
	pluginsJS =  and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 10.376735%, instances = 283: 
	sessionJS = yes and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 32.699934%, instances = 765: 
	sessionJS = yes and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 20.434265%, instances = 182: 
	vendorWebGLJS = Not supported and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 42.058299%, instances = 490: 
	vendorWebGLJS = Not supported and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 86.302796%, instances = 304: 
	vendorWebGLJS = Not supported and userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36

	Soft Paradox detected
	confidence = 8.892356%, instances = 141: 
	dntJS = NC and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 28.432137%, instances = 438: 
	dntJS = NC and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 10.375878%, instances = 283: 
	localJS = yes and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 32.705494%, instances = 765: 
	localJS = yes and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 16.777267%, instances = 133: 
	encodingHttp = gzip, deflate, sdch, br and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 28.654075%, instances = 305: 
	encodingHttp = gzip, deflate, sdch, br and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 99.931938%, instances = 11: 
	encodingHttp = gzip, deflate, sdch, br and platformJS = iPad

	Soft Paradox detected
	confidence = 13.683413%, instances = 135: 
	resolutionFlash = Flash not detected and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 31.961626%, instances = 493: 
	resolutionFlash = Flash not detected and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 14.679937%, instances = 306: 
	IEDataJS = no and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 36.266305%, instances = 884: 
	IEDataJS = no and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 26.640927%, instances = 90: 
	webGLJs = Not supported and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 50.096525%, instances = 259: 
	webGLJs = Not supported and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 78.474903%, instances = 180: 
	webGLJs = Not supported and userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36

	Soft Paradox detected
	confidence = 14.679937%, instances = 306: 
	octaneScore =  and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 36.266305%, instances = 884: 
	octaneScore =  and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 29.881040%, instances = 338: 
	hostHttp = amiunique-backend and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 45.603385%, instances = 1223: 
	hostHttp = amiunique-backend and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 13.043478%, instances = 2: 
	canvasJSHashed = da39a3ee5e6b4b0d3255bfef95601890afd80709 and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 52.173913%, instances = 4: 
	canvasJSHashed = da39a3ee5e6b4b0d3255bfef95601890afd80709 and userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36

	** Hard Paradox detected **
	confidence = 100.000000%, instances = 4: 
	canvasJSHashed = da39a3ee5e6b4b0d3255bfef95601890afd80709 and platformJS = iPad
	platformJS must be either of the followings: 
	[u'Win32', u'Linux armv8l', u'Linux armv7l', u'MacIntel']

	Soft Paradox detected
	confidence = 19.559734%, instances = 91: 
	pluginsJSHashed = da39a3ee5e6b4b0d3255bfef95601890afd80709 and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 37.858289%, instances = 303: 
	pluginsJSHashed = da39a3ee5e6b4b0d3255bfef95601890afd80709 and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 26.640927%, instances = 90: 
	webGLJsHashed = 8e635455c1c04acc72cc3cb8b3930fa2002922c7 and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 50.096525%, instances = 259: 
	webGLJsHashed = 8e635455c1c04acc72cc3cb8b3930fa2002922c7 and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 78.474903%, instances = 180: 
	webGLJsHashed = 8e635455c1c04acc72cc3cb8b3930fa2002922c7 and userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36

	Soft Paradox detected
	confidence = 20.434265%, instances = 182: 
	rendererWebGLJS = Not supported and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 42.058299%, instances = 490: 
	rendererWebGLJS = Not supported and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 86.302796%, instances = 304: 
	rendererWebGLJS = Not supported and userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36

	Soft Paradox detected
	confidence = 90.789474%, instances = 9: 
	platformJS = iPad and languageHttp = en-US,en;q=0.8

	Soft Paradox detected
	confidence = 9.210526%, instances = 3: 
	platformJS = iPad and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 91.447368%, instances = 6: 
	platformJS = iPad and orderHttp = Upgrade-Insecure-Requests Referer Connection Accept X-Real-IP Accept-Language Accept-Encoding User-Agent Host

	Soft Paradox detected
	confidence = 11.842105%, instances = 5: 
	platformJS = iPad and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1

	Soft Paradox detected
	confidence = 96.052632%, instances = 2: 
	platformJS = iPad and resolutionJS = 360x640x32

	Soft Paradox detected
	confidence = 78.947368%, instances = 10: 
	platformJS = iPad and canvasJS = 

	Soft Paradox detected
	confidence = 72.368421%, instances = 9: 
	platformJS = iPad and userAgentHttp = Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36

	Soft Paradox detected
	confidence = 96.710526%, instances = 1: 
	platformJS = iPad and encodingHttp = gzip, deflate, sdch, br

	Soft Paradox detected
	confidence = 78.947368%, instances = 10: 
	platformJS = iPad and canvasJSHashed = da39a3ee5e6b4b0d3255bfef95601890afd80709

	Soft Paradox detected
	confidence = 14.679937%, instances = 306: 
	sunspiderTime =  and id = cde0cf74-70e2-4a40-9a6c-4703f9c2557b

	Soft Paradox detected
	confidence = 36.266305%, instances = 884: 
	sunspiderTime =  and addressHttp = 7f6b9228e8c60669fff2ff610af55b67e0f43ce1
