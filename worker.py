import os

if __name__ == '__main__':
    print('Running `pipenv install`')
    os.system('pipenv install')
    print('Running `pipenv install --dev`')
    os.system('pipenv install --dev')
    # os.system('python main.py')
    print('Running `python another_file.py`')
    os.system('python another_file.py')