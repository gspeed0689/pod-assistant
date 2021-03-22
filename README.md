# pod-assistant
Old python utility to assist with making a Bentley Pod Creator conversion project file. 

This Python 2.7 utility was made when I was a graduate student to solve an issue with the Bentley Pod Creator. The issue with the program was that when trying to add point cloud files to the conversion software, it would not add all of the files, and subsequent file adding porcesses would still fail to add all of the files. This python utility would create a Bentley Pod Creator compliant XML file with all of the desired point cloud files, the Bentley Pod Creator software would then convert all of the files. 

**Usage**

In its current state there are only two command line arguments active, `-d` for directory, and `-t` for type of point cloud. `-d` is the directory of all of the point cloud tiles, and `-t` is the type of point cloud, either `las` or `laz`. When running the script, it will list all of the files in the directory of the `-t` type specified, and write a `.pbp` xml file to that same directory.  

**Future Fixes**

Had Bentley not fixed their software, I could have extended the script to use all of the options available in the software. I had already populated the command line argument parser with all of the other options available in the software. 
