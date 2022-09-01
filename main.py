import Parser
from command_function import commandfactory


if __name__=='__main__':
    args = Parser.parseInput()
    command = commandfactory.build_command(args)
    command.excute()