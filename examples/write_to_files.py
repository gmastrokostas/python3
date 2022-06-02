import os
base_path = '/home/seeker/LOL'
f_name = 'test_file.txt'

full_fn = base_path+'/'+f_name

#f = open(full_fn, 'w')

with open(full_fn, 'a') as f:
    f.write("Line one\n")
    f.write("Line two\n")

