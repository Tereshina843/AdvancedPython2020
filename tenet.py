from os.path import isdir

def tenet(input_file_path: str, output_file_path: str) -> None:
    if isdir(input_file_path):
        raise ValueError(input_file_path + "is a directory")
    if input_file_path == output_file_path:
        raise ValueError("The output is the same as input")
    readfile = open(input_file_path, "r")
    writefile = open(output_file_path, "w")
    for s in readfile.readlines():
        writefile.write((s.strip('\n'))[::-1] + '\n')
    readfile.close()
    writefile.close()

if __name__ == '__main__':
    tenet("input.txt", "output.txt")