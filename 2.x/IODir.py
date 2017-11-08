import os

print 'OS name:', os.name

print 'os.environ:', os.environ

print "os.PATH:", os.getenv("path")

# current the dir's absolute
print "absolute the dir:", os.path.abspath('.')

# new a dir in a special dir
newdir = os.path.join('E:\WorkSpace\PycharmProjects\PythonStudy', 'testdir')
os.mkdir(newdir)
# delete the dir
os.rmdir(newdir)

# split the dir
print os.path.split('E:\WorkSpace\PycharmProjects\PythonStudy')

# export the extend name
print os.path.splitext('README.MD')

# rename the file
# os.rename('hello.txt', 'newhello.txt')
# os.remove('newhello.txt')

# list all the dirs that start with '.'
print [x for x in os.listdir('.') if os.path.isdir(x)]

# list all the py files
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']


