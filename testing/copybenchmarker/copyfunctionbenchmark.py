import re

def copytimes():
    metadata = []
    nometadata = []

    with open('testing/metadata.txt', 'r') as f:
        with_metadata = f.readlines()
        for data in with_metadata:
            float_getter = re.compile(r'\d+\.\d+')
            metadata.append(float_getter.findall(data))
        fixed_list = [float(element[0]) for element in metadata]
        print(f'Metadata Files: {len(with_metadata)}.')
        print(f'Metadata: {sum(fixed_list) / len(fixed_list):0.4f} sec avg. (per file).')
        print(f'Metadata: {sum(fixed_list):0.4f} sec total\n')

    with open('testing/nometadata.txt', 'r') as f:
        without_metadata = f.readlines()
        for data in without_metadata:
            float_getter = re.compile(r'\d+\.\d+')
            nometadata.append(float_getter.findall(data))
        fixed_list = [float(element[0]) for element in nometadata]
        print(f'No Metadata Files: {len(without_metadata)}.')
        print(f'No Metadata: {sum(fixed_list) / len(fixed_list):0.4f} sec avg. (per file) for {len(without_metadata)} files.')
        print(f'No Metadata: {sum(fixed_list):0.4f} sec total')

if __name__ == '__main__':
    copytimes()