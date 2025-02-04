Updated Version (2017.12.23)

**Original repository:**
CYKITV2: https://github.com/CymatiCorp/CyKITv2
CYTHON-HIDAPI: https://github.com/trezor/cython-hidapi

 - for Python3.9 (Linux)

Python Data Controller for Neural EEG headsets.


# Description

Streams EEG data to a browser for data handling.
Works with Chrome and Firefox thus far.

# Dependencies

See [requirements.txt](./requirements.txt).
<!-- * pywinusb 0.4.2 --- https://pypi.python.org/pypi/pywinusb/  <br>
* pycrypto 2.6.1 --- https://pypi.python.org/pypi/pycrypto/2.6.1
//-->
1. Clone this and Cython-Hidapi repositories and include cython-hidapi as subfolder.

2. Install: hidapi, hid, cython-hidapi, pyhidapi (optional).

3. Replace ad hoc paths included in Python files.

# Usage

Example 1.
`python CyKITv2.py 127.0.0.1 18675 2`

Example 2.
`python CyKITv2.py 127.0.0.1 15309 4 info`

Example 3.
`python CyKITv2.py 127.0.0.1 12991 6 info+confirm`

*Thanks to the authors.*
 
* Feel free to offer comments and suggests via Issues, for further <br>
information check our Discord server.  Submit new push requests,  <br>
if you have something to contribute. <br>
