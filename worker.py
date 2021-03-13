import os

if __name__ == '__main__':
    os.system('pipenv install')
    os.system('pipenv install --dev')
    os.system('pipenv run pytest tests')