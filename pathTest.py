from pathlib import  Path

#absolute path => from root path
#relative path => from current path

# path = Path("emails")
# # print(path.mkdir())
# print(path.rmdir())

path = Path()
for file in path.glob('*.py'):
    print(file)