import yaml, json

# def json_to_yaml(file_name):
#     with open(file_name+'.json', 'r') as json_in, open(file_name+'.yaml', 'w') as yaml_out:
#         json_payload = json.load(json_in)
#         yaml.dump(json_payload, sort_keys=False)

import json
import yaml


def do_json_to_yaml(filename):
        pass
        print('do json to yaml')
        f = open(filename)
        # step 2
        data = json.loads(f.read())
        ## print(type(data), data)

        # step 3
        ## converts to a yaml string
        tdata = yaml.dump(data)
        output_filename = filename.replace('.json', '.yaml')
        output_file = open(output_filename, "w")
        output_file.write(tdata)
        # cleanup
        f.close()
        output_file.close()

if __name__ == '__main__':
        filename = "emojis.json"
        do_json_to_yaml(filename)

# json_to_yaml('donuts')
json_to_yaml('emojis')