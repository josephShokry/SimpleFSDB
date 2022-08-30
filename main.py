import Parser
import commands_function


if __name__=='__main__':
    args=Parser.parseInput()
    command =commands_function.commandfactory.build_command(args)
    command.excute()
    