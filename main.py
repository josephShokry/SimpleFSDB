import Parser
import command_function


if __name__=='__main__':
    args=Parser.parseInput()
    command =command_function.commandfactory.build_command(args)
    command.excute()
    