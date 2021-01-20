from .utils import arg_to_attr, attr_to_arg


class ArgumentHandler:

    def __init__(self, args):
        """
        Get CLI arguments as Argument objects, pass them to argparse and validate relationships

        :param args: list of Argument objects instances
        """
        self.__arguments = args
        self.__get_args()
        self.__validate_args()

    def __get_args(self):
        """
        Pass the Argument objects instances to argparse
        """
        from argparse import ArgumentParser

        self.__parser = ArgumentParser()
        for arg in self.__arguments:
            arg_to_dict = arg.to_dict()
            self.__parser.add_argument(*arg.argname, **arg_to_dict['arg_details'])
        self.args = self.__parser.parse_args()

    def __get_argument_by_arg_name(self, arg_name):
        """
        Search and return an Argument object instance

        :param arg_name: the argument name of object to search
        :return: the Argument object instance
        """
        for arg in self.__arguments:
            if arg_name in arg_to_attr(arg.arg_name):
                return arg

    def __validate_args(self):
        """
        Scan arguments an check the relationships
        """
        for arg, value in self.args.__dict__.items():
            if not value:
                continue

            mapped_arg = self.__get_argument_by_arg_name(arg).to_dict()
            for rel in mapped_arg.keys():
                if rel != 'arg_details':
                    getattr(self, rel)(arg, mapped_arg[rel])

    def require(self, arg, requirements):
        """
        Check if the argument requirements are defined

        :param arg: the arg to check
        :param requirements: the list of requirements to find
        """
        for req in requirements:
            if not getattr(self.args, arg_to_attr(req)):
                self.__parser.error('{} requires {}'.format(attr_to_arg(arg), req))

    def conflict(self, arg, conflicts):
        """
        Check if the argument conflicts are not defined

        :param arg: the argument to check
        :param conflicts: the list of requirements to find
        """
        for con in conflicts:
            if getattr(self.args, arg_to_attr(con)):
                self.__parser.error('{} conflicts with {}'.format(attr_to_arg(arg), con))

    def dependency(self, arg, dependencies):
        """
        Check if a least one of the argument dependencies is satisfied

        :param arg: the argument to check
        :param dependencies: the list of dependencies to find
        """
        if len([d for d in dependencies if getattr(self.args, arg_to_attr(d))]) < 1:
            self.__parser.error('{} need at least one from {}'.format(attr_to_arg(arg), ', '.join(dependencies)))
