import re

def copytimes():
    metadata = []
    nometadata = []

    with open('version_0-9.txt', 'r') as f:
        with_metadata = f.readlines()
        for data in with_metadata:
            float_getter = re.compile(r'\d+\.\d+')
            metadata.append(float_getter.findall(data))
        fixed_list = [float(element[0]) for element in metadata]
        print(f'Old alg: {sum(fixed_list) / len(fixed_list):0.4f} sec avg. (per file) for {len(with_metadata)} files.')

    with open('version_1-0.txt', 'r') as f:
        without_metadata = f.readlines()
        for data in without_metadata:
            float_getter = re.compile(r'\d+\.\d+')
            nometadata.append(float_getter.findall(data))
        fixed_list = [float(element[0]) for element in nometadata]
        print(f'New alg: {sum(fixed_list) / len(fixed_list):0.4f} sec avg. (per file) for {len(without_metadata)} files.')

if __name__ == '__main__':
    copytimes()