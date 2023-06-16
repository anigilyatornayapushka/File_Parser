import sys
import os


def find_file(path: str) -> None:

    file: str = os.path.split(path)[-1]
    if file.split('.')[-1] == 'py':
        print(path)


def parse(directory: str | list[str]) -> None:

    if isinstance(directory, list):
        d: str
        for d in directory:
            parse(d)

    else:
        if os.path.isdir(directory):

            d: str
            for d in os.listdir(directory):
                parse(os.path.join(directory, d))

        else:
            find_file(directory)


def main():
    match sys.argv:
        case _, *directories if len(directories) > 0:
            parse(directories)
        case _:
            parse(os.listdir())


if __name__ == '__main__':
    main()
