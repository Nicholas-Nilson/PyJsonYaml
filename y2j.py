import yaml, json

def yaml_to_json(file_name):
    with open(file_name+'.yaml', 'r') as file:
        configuration = yaml.safe_load(file_name)

    with open(file_name+'.json', 'w') as json_file:
        json.dump(configuration, json_file)

# yaml_to_json'verify')
yaml_to_json('xmas')