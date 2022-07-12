import yaml, json

def json_to_yaml(file_name):
    with open(file_name+'.json', 'r') as json_in, open(file_name+'.yaml', 'w') as yaml_out:
        json_payload = json.load(json_in)
        yaml.dump(json_payload, sort_keys=False)


# json_to_yaml('donuts')
json_to_yaml('emojis')