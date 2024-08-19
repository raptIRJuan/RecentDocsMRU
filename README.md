# RecentDocsMRU
This script will parse the RecentDocs key and its subkeys in a NTUSER.dat file. It will output the list of filenames in order with the associated timestamps. See Dan's ([@4n6k](https://twitter.com/4n6k)) [blog post](http://www.4n6k.com/2014/02/forensics-quickie-pinpointing-recent.html) for background. Usage is simple. Only the `-f` option is required to specify the NTUSER.dat file of interest. If no other option is used, output will be to the console. If the `-o` option is used, the output will be written to the file specified. 

####Note: the output to file is in Unicode. 
Notepad in windows and textEdit in OS X will open the file and display it without any issues, as should any text editors that can handle UTF-16. This is to handle foreign characters in filenames. Due to the windows command prompt not properly displaying Unicode, the 0x00 bytes are removed from the output to console. For most cases where the file name is in English, this won't be a problem. However, if there are filenames with foreign characters you should use the `-o` option.

#Requirements
This script uses Willi Ballenthin's python-registry: https://github.com/williballenthin/python-registry

#Usage Examples
Output to console:
```
recentdocs-mru.py -f NTUSER.DAT
```
Output to a file named output.txt
```
recentdocs-mru.py -f NTUSER.DAT -o output.txt
```

#Credit
* This is not an original idea. Eric Opdyke ([@EricOpdyke](https://twitter.com/EricOpdyke)) created a similar script long ago. You can find it here: https://github.com/eopdyke/RecentDocs-MRU-Parser. However, Eric's script needs to be run on Windows due to the use of python's winreg module. I wanted something that I could run on OS X, or Ubuntu, as well as Windows.
* Willi Ballenthin ([@williballenthin](https://twitter.com/williballenthin)) for his python-registry project. It makes pulling keys and values from the registry easy. 
* Dan ([@4n6k](https://twitter.com/4n6k)) for a great [post](http://www.4n6k.com/2014/02/forensics-quickie-pinpointing-recent.html) regarding this artifact. 
* drwicid (https://github.com/drwicid) for updating the script for python 3. 
