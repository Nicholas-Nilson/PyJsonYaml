import yaml, json

def JSON_to_Yaml(file_name):
    with open(file_name+'.yaml', 'r') as file:
        configuration = yaml.safe_load(file_name)

    with open(file_name+'.json', 'w') as json_file:
        json.dump(configuration, json_file)

# JSON_to_Yaml('verify')
JSON_to_Yaml('xmas')