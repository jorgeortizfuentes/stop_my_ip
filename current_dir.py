import os
directory_path = os.getcwd()
print("My current directory is : " + directory_path)

# Directory where is this script
directory_script = os.path.dirname(os.path.realpath(__file__))
print("My script directory is : " + directory_script)
