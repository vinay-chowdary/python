#! /usr/bin/python3
# using custom interpreter like in shell scripting.we can chmod of
# this file and can be executed as ./helloworld.py

from importlib import reload
from os import getcwd  # getcwd is function which displays current working dir
from sys import platform    # platform is a string which carries type of os

# this particular import line produces bytecode for the file that is getting imported
# byte code is created only when script/module/file is imported
import toImportInHelloWorldScript as importedFile

# loading imported script again
reload(importedFile)


# printing the names in imported file , form of __X__  are built-in names
print(dir(importedFile))
print(importedFile.b, importedFile.c)


# to print hello world on console
print("hello world! Let's begin writing python code")

# calculate floors
inp = input("Europe floor? ")
#  TODO: deal with bad inputs later
usf = int(inp)+1
print("us floor", usf)


# sep is separator while displaying
print(getcwd(), platform, sep="\n")

# declaring a variable is not required we can directly refer it or define it
var = "hello"

# multiplying string is equal to concatenating itself
print(var*2, "spam!"*6, sep="-->")

# loop basics
for char in "string or iterator or list or tuple and so on":
    print(char, end=",")

print()

# executinng other files ( only python files ) using exec()
# exec(open('test.sh').read()) will not be executed
exec(open('toImportInHelloWorldScript.py').read())


# c programs can run python by including header : pgno 82 in TB( O'REILLY )
# include <Python.h>
# Py_Initialize();
# print("hello")

# getting help
help(var.join)

print(type(var), id(var))
