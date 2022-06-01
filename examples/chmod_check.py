import os


def check_x(f_path):
    x_status = os.access(f_path, os.X_OK)
    if x_status == False:
        print(f_path, "Directory Cannot be accessed. Quiting")

f_path='/home/ansible/tmp_2'
check_x(f_path)

############################################################################
f_path = ('test_file.txt')
#check_file_1 = os.access(f_path, os.X_OK)
#check_file_2 = os.access(f_path, os.F_OK)
#check_file_3 = os.access(f_path, os.F_TEST)
#check_file_4 = os.access(f_path, os.W_OK)

status = os.stat(f_path)
chmod_status = oct(status.st_mode)[-3:]

if chmod_status != 750:
    print("file change will not work. Changing the chmod on this file")
    os.chmod(f_path, 0o750)
else:
    print("exiting")




