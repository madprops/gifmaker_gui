import sys


def msg(message):
    print(message, file=sys.stderr)


def respond(message):
    print(message, file=sys.stdout)
