# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:20:37 2019

@author: MabuXayda
"""

"""
PYTHON MODULES

- Consider a module to be the same as a code library.
- A file containing a set of functions you want to include in your application.
- To create a module just save the code you want in a file with the file 
extension .py
- Now we can use the module we just created, by using the import statement
- You can create an alias when you import a module, by using the as keyword.
- Import module trigger execution for whole module file
"""
from tutorial import day4 as d #from Package import Module.py as Variable
d.test_module_day4()

from Lesson import day4_Loop as d
d.test_module_day4()

"""
FILE HANDLING

- For file handling, we use OS module
    + use os.mkfir() to create folder
    + use os.rmdir() to delete folder
    + use os.remove() to remove file
    + use os.path.exists() to check if file exists

  - os.path is either posixpath or ntpath
  - os.name is either 'posix' or 'nt'
  - os.curdir is a string representing the current directory (always '.')
  - os.pardir is a string representing the parent directory (always '..')
  - os.sep is the (or a most common) pathname separator ('/' or '\\')
  - os.extsep is the extension separator (always '.')
  - os.altsep is the alternate pathname separator (None or '/')
  - os.pathsep is the component separator used in $PATH etc
  - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
  - os.defpath is the default search path for executables
  - os.devnull is the file path of the null device ('/dev/null', etc.)
"""
import os
os.mkdir("F:/temp/NordicCoder/python_analysis/test_os")
os.rmdir("F:/temp/NordicCoder/python_analysis/test_os")
os.getcwd()

"""
- To open the file, use the built-in open() function.
- The open() function returns a file object, which has a read() method for 
reading the whole content of the file
- The open() function takes two parameters; filename, and mode.
    + "r" - Read - Default value. Opens a file for reading, error if the 
    file does not exist
    + "a" - Append - Opens a file for appending, creates the file if it 
    does not exist
    + "w" - Write - Opens a file for writing, creates the file if it 
    does not exist
    + "x" - Create - Creates the specified file, returns an error if the 
    file exists
- In addition you can specify if the file should be handled as binary or 
text mode
    + "t" - Text - Default value. Text mode
    + "b" - Binary - Binary mode (e.g. images)
"""

f = open("F:/temp/NordicCoder/python_analysis/tutorial/ggapp_sample.csv", "rt")
print(f.read())

"""
- You can return one line by using the readline() method.
- By looping through the lines of the file, you can read the whole file, 
line by line
- It is a good practice to always close the file when you are done with it.
"""
f = open("F:/temp/NordicCoder/python_analysis/tutorial/ggapp_sample.csv")
print(f.readline())
print(f.readline())

f = open("F:/temp/NordicCoder/python_analysis/tutorial/ggapp_sample.csv")
for x in f:
    print(x)
f.close()

"""
- To create a new file in Python, use the open() method, with one of the 
parameters a, w or x
- To write to an existing file, you must add parameter(a or w) to the open() 
function.
- Using write() to write content to file
- Remember to close the file
"""
file_path = "F:/temp/NordicCoder/python_analysis/tutorial/new_file.txt"
f = open(file_path, "x")

f = open(file_path, "a")
f.write("This is just some text sample")
f.close()