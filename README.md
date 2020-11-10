# pwlistgen - written in python
**pwlistgen** is a password list generator for numerical passwords, with a length of your choice.
## Requirements
The only thing you need is to **install the latest version of Python** (and of course **`pwlistgen.py`**) on your PC, in order to execute the code. This works on all operating systems, so head over to https://www.python.org/download and install Python for your OS of choice.

To check if Python is already installed, type:
```cmd
py --version
```
If Python does respond, consider that you've installed the latest version (see https://www.python.org/download#content). If it doesn't respond, you have to install it first.
## Preparation
Since the installation of Python is done, open your cmd and refer to the path (starting from your **home directory**) where `pwlistgen.py` is located:
```cmd
cd thePath/pwlistgen/isLocated
```
Or in my case:
```cmd
cd Desktop/pwfolder
```
## Executing
Now that you are in the folder where you've installed **pwlistgen**, type:
```cmd
py pwlistgen.py > yourFileName.xy
```
Or in my case:
```cmd
py pwlistgen.py > pwlist.txt
```
Or if want to save it in a different *(already existing)* path:
```cmd
py pwlistgen.py > ../github/pwlist.txt
```
## Generate
Last but not least type in the **length of your password**, hit **enter**, **wait** and it will create a password list for the entered length in the path/file you specified.\
\
PS: I don't recommend entering a larger number than 10 – except you know exacly what you're doing – since the 8-characters password list is already 1 GB large and does take some time to create.

PPS: If `py` doesn't work in your cmd try to type in `python` instead.
