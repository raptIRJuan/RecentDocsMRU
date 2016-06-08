# RecentDocsMRU
This script will parse the RecentDocs key and its subkeys in a NTUSER.dat file. Usage is simple. Only the `-f` option is required to specify the NTUSER.dat file of interest. If no other option is used, output will be to the console. If the `-o` option is used, the output will be written to the file specified. 

####Note: the output to file is in Unicode. 
Notepad in windows and textEdit in OS X will open the file and display it without any issues, as should any text editors that can handle UTF-16. This is to handle foreign characters in filenames. Due to the windows command prompt not properly displaying Unicode, the 0x00 bytes are removed from the output to console. For most cases where the file name is in English, this won't be a problem. However, if there are filenames with foreign characters you should use the `-o` option.

#Usage Examples
Output to console:
```
recentdocs-mru.py -f NTUSER.DAT
```
Output to a file named output.txt
```
recentdocs-mru.py -f NTUSER.DAT -o output.txt
```
