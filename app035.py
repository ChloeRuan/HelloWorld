# work directly with python
# absolute path
# c:\Program Files\Microsoft, MAX:/user/local/bin
# Relative path, this tutorial


from pathlib import Path

path = Path("ecommerce")
print(path.exists())
print(path.glob(
    '*.py'))  # * means everything, glob searches current directories, path and files, to get all teh files type:*.*
for file in path.glob('*.py'):
    print(file)

"""
for file in path.glob('*'):        #search all the directories
    print(file)
"""

# when the directory doesnt exist

path1 = Path("email")
"""
print(path1.mkdir())    #mkdir = make directtory
print(path1.rmdir())    #rmdir= remove directory
"""
