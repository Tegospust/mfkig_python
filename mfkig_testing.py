#!/usr/bin/python
# !/usr/bin/env/python


import os


def main(args):
    with open("c:\\_temp_\\mfkig.txt", "r") as file:
            lines = []
            tuples = []
            for line in file:
                lines.append(line.rstrip())
                tuples.append((int(line.split("=")[0]), line.split("=")[1].rstrip()))
                t_sorted_by_name = sorted(tuples,key = lambda x: x[1])
                t_sorted_by_num = sorted(tuples,key = lambda x: x[0])


            print(t_sorted_by_num)

    # print(f'{args[0]} - testing...') # wyświetl nazwę pliku
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main(sys.argv))
