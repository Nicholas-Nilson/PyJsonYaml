import yaml, json


def do_yaml_to_json(filename):
    print('do yaml to json')
    f = open(filename)
    data = yaml.safe_load(f.read())
    temp_data = json.dumps(data)
    output_filename = filename.replace('.yaml', '.json')
    output_file = open(output_filename, 'w')
    output_file.write(temp_data)

    f.close()
    output_file.close()


# def yaml_to_json(file_name):
#     with open(file_name+'.yaml', 'r') as file:
#         configuration = yaml.safe_load(file_name)
#
#     with open(file_name+'.json', 'w') as json_file:
#         json.dump(configuration, json_file)

# yaml_to_json'verify')
yaml_to_json('xmas')