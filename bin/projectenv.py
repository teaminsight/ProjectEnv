import os
import sys

projectenv_lib_path = os.path.join(os.getenv('PROJECTENV_HOME'), 'lib')
sys.path = [projectenv_lib_path] + sys.path # lib dir should be first in path

from logger import log, error, DEBUG
import commands

COMMANDS = {
    'init': commands.init,
    'sync': commands.sync
}

def main():
    if DEBUG:
        log('debug', str(True))

    if len(sys.argv) < 2:
        error('usage')
    elif sys.argv[1].lower() in COMMANDS:
        COMMANDS[sys.argv[1].lower()](*sys.argv[2:])
    else:
        error('unknown_command', 'unkown command: %s' % sys.argv[1])

if __name__ == '__main__':
    main()
