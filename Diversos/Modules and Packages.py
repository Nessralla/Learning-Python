# __main__

# Most Python code is either a module to be imported, or a script that does something.
# However, sometimes it is useful to make a file that can be both imported as a module and run as a script.
# To do this, place script code inside if __name__ == "__main__".
# This ensures that it won't be run if the file is imported.
# Example:
def function():
    print("This is a module function")

if __name__=="__main__":
    print("This is a script")

# When the Python interpreter reads a source file, it executes all of the code it finds in the file. 
# Before executing the code, it defines a few special variables.
# For example, if the Python interpreter is running that module (the source file) as the main program, 
# it sets the special __name__ variable to have a value "__main__". If this file is being imported from 
# another module, __name__ will be set to the module's name.

import this


# Packaging


# In Python, the term packaging refers to putting modules you have written in a standard format, 
# so that other programmers can install and use them with ease.
# This involves use of the modules setuptools and distutils.

# The first step in packaging is to organize existing files correctly. Place all of the files you want 
# to put in a library in the same parent directory. This directory should also contain a file called __init__.py, 
# which can be blank but must be present in the directory.

# This directory goes into another directory containing the readme and license, as well as an important file called setup.py.
# Example directory structure:

# SoloLearn/
#    LICENSE.txt
#    README.txt
#    setup.py
#    sololearn/
#       __init__.py
#       sololearn.py
#       sololearn2.py


# The next step in packaging is to write the setup.py file.
# This contains information necessary to assemble the package so it can be uploaded to PyPI and installed 
# with pip (name, version, etc.).
# Example of a setup.py file:

from distutils.core import setup

setup(
   name='SoloLearn', 
   version='0.1dev',
   packages=['sololearn',],
   license='MIT', 
   long_description=open('README.txt').read(),
)

# After creating the setup.py file, upload it to PyPI, or use the command line to create a binary distribution
#  (an executable installer).

# To build a source distribution, use the command line to navigate to the directory containing setup.py, 
# and run the command python setup.py sdist.

# Run python setup.py bdist or, for Windows, python setup.py bdist_wininst to build a binary distribution.
# Use python setup.py register, followed by python setup.py sdist upload to upload a package.