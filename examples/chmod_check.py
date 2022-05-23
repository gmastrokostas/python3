import os


def check_x(f_path):
    x_status = os.access(f_path, os.X_OK)
    if x_status == False:
        print(f_path, "Directory Cannot be accessed. Quiting")

f_path='/home/ansible/tmp_2'
check_x(f_path)


