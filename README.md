Updated Version (2025.02.04)

**Original repository:**
CYKITV2: https://github.com/CymatiCorp/CyKITv2
CYTHON-HIDAPI: https://github.com/trezor/cython-hidapi

 - for Python3.9 (Linux)
 - Mac OS (Sonoma guaranteed)

Python Data Controller for Neural EEG headsets.


# Description

Streams EEG data to a browser for data handling.
Works with Chrome and Firefox thus far.

# Dependencies

See [requirements.txt](./requirements.txt).


1. Clone this and Cython-Hidapi repositories and include cython-hidapi as subfolder.

2. Install: hidapi, hid, cython-hidapi, pyhidapi (optional).

3. Replace ad hoc paths included in Python files.

# Usage

Example 1. No web view - only EEG csv
`python CyKITv2.py 127.0.0.1 18675 2 outputdata+noweb`

Example 2. Web view - info
`python CyKITv2.py 127.0.0.1 15309 4 info`

Example 3. 
`python CyKITv2.py 127.0.0.1 12991 6 outputdata+info+confirm`
See opt. for details.

*Thanks to the authors of cited links.*
 
* Feel free to offer comments and suggests via Issues, for further <br>
information check our Discord server.  Submit new push requests,  <br>
if you have something to contribute. <br>
