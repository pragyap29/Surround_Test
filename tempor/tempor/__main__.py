import argparse
from surround import Assembler
from stages import Main, ValidateData
from batch_runner import BatchRunner
from web_runner import WebRunner


def main():
    parser = argparse.ArgumentParser(prog='Tempor', description="Surround mode(s) available to run this module")
    parser.add_argument('--mode', help="Mode to run (train, batch)", default="web")
    execute_assembler(parser.parse_args().mode)


def execute_assembler(mode):
    assembler = Assembler("Default project", ValidateData(), Main())
    if mode == "train":
        BatchRunner(assembler).run(True)
    elif mode == "batch":
        BatchRunner(assembler).run()
    else:
        WebRunner(assembler).run()


if __name__ == "__main__":
    main()
