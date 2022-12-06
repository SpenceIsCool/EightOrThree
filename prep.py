# prep.py


import os
import kaggle
from zipfile import ZipFile


if __name__ == '__main__':
    project = os.getcwd()
    print(project)

    # dirs = ['models', 'datasets', 'results']
    # for d in dirs:
    d = f'{project}/results'
    if not os.path.exists(d):
        os.makedirs(d)
    else:
        print(f'{d} already exists')

    zip_file_path = f'{project}/asl-isl-numbers-conversions.zip'
    if not os.path.exists(zip_file_path):
        os.system(f'cd {project} ; kaggle datasets download -d spenceiscool/asl-isl-numbers-conversions')
        with ZipFile(zip_file_path, 'r') as z_obj:
            z_obj.extractall(path=project)
        print("hi")
    else:
        print(f'File already exits: {zip_file_path}')
        print('If you think this is an error, please delete the file and re-run me.')


