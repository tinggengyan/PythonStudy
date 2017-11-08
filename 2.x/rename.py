import os

path = os.getcwd()

i = 1
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)) == True:
        if file.find('.py') > 0:
            continue
        else:
            newname = str(i) + '.png'
            os.rename(os.path.join(path, file), os.path.join(path, newname))
            i = i + 1
