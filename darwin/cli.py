import sys
import darwin


def main():
    if "--version" in sys.argv:
        print(darwin.__version__)
        sys.exit(0)

    sys.exit(0)
