from os import linesep

def save_lines_to_file(file_path: str, lines: list)->bool:
    with open(file_path, 'w') as f:
        f.write(linesep.join(lines))


def strip_empty_rows(subject: list)->list:
    return [x for x in subject if len(x) > 0]


def get_lines_from_file(file_path: str)->list:
    with open(file_path, 'r') as f:
        return f.read().splitlines()
