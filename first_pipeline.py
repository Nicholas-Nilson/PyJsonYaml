import json
import yaml
import sys


def is_yaml(filename):
    return '.yaml' in filename


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
    # filename = "xmas.yaml"
    if len(sys.argv) != 2:
        print("you forgot the filename!")
        exit()
    filename = sys.argv[1]
    if is_yaml(filename):
        do_yaml_to_json(filename)
    else:
        do_json_to_yaml(filename)
