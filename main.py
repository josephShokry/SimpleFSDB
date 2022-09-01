import Parser
import Commandfactory

if __name__=='__main__':
    args = Parser.parseInput()
    command = Commandfactory.Command_Factory.build_command(args)
    command.execute()