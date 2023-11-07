import yaml


def read_yaml(filepath):
    with open(filepath, 'r') as file:
        data = yaml.safe_load(file)
        print(data['ENTER_NAME'])



