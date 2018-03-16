#!/usr/bin/env python

import kookoo



# The same XML can be created above using the convenience methods
r = kookoo.Response()
r.addPlayText("Hello World")
r.addPlayAudio("http://www.mp3.com")
r.addRecord("test.wav",maxDuration="30",silence="3");
print(r);


""" outputs:
<Response>
	<PlayText>Hello World</PlayText>
	<PlayAudio>http://www.mp3.com</PlayAudio>
	<Record maxduration="30" silence="3">test.wav</Record>
</Response>
"""


# ===========================================================================
# Using Conference
r = kookoo.Response()
r.addPlayText("Welcome to the conference")
r.addConference("12345",caller_onhold_music="default",record="true",caller_id="",timeout="-1",version="1")
print(r);

""" Outputs:
<Response>
	<PlayText>Welcome to the conference</PlayText>
	<Conference>12345</Conference>
</Response>
"""

# ===========================================================================
# Using Dial Tag
r = kookoo.Response()
r.addDial('9XXXXXX',record='true',limittime="1000",timeout="30",moh='default',promptToCalledNumber='no',caller_id='9180XXXXXX')
print(r);

""" Outputs:
<Response>
	<dial record="true" limittime="1000" timeout="30" moh="default" promptToCalledNumber="no" caller_id="9180XXXXXX">9XXXXXX</dial>
</Response>
"""


# ===========================================================================
# Collecting user input
r = kookoo.Response()
r.append(kookoo.CollectDtmf(maxDigits=1,timeout=4,
	termchar="#"))
r.append(kookoo.PlayText("Press 1 followed by hash"))
print(r);

""" outputs:

<Response>
	<CollectDtmf l="1">
		<PlayText>Press 1</PlayText>
	</CollectDtmf>
</Response>


"""

# ===========================================================================
# Using voice recognition tag
r = kookoo.Response()
r.addRecognize(type="zena",timeout="5", silence="10",lang="en",length="1",grammar="digits")
print(r);

""" Outputs:
<Response>
	<Recognize type="zena" timeout="5" silence="10" lang="en" length="1" grammar="digits"/>
</Response>
"""
