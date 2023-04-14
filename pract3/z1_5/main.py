def load_config(filename):
    f = open(filename, 'r').read()
    exec(f, globals())

load_config('config.py')
print(NAME)
print(MAIL)
