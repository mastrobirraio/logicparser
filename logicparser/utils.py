class DictObject:

    def __init__(self, **kwargs):
        """
        Get all the parameter as dict and save it has object

        :param kwargs: a dict with keys and values
        """
        self.__dict__ = kwargs


class Argument(DictObject):

    def __init__(self, **kwargs):
        """
        Allow to transform a dict to an object and validate used fields

        :param kwargs: a dict with keys and values
        """
        super(Argument, self).__init__(**kwargs)
        self.__allowed_attrs = {
            'required': ('arg_name',),
            'arg_details': ('metavar', 'action', 'help', 'nargs',),
            'arg_relations': ('require', 'conflict', 'dependency',)
        }
        self.__validate_args()

    @property
    def argname(self):
        name = self.arg_name
        return (name,) if isinstance(name, str) else name

    @property
    def __declared_attrs(self):
        """
        Obtain the list of attributes that can be considerate valid

        :return: the list with attributes names
        """
        return [attr_name for attr_name in self.__dict__.keys() if not attr_name.startswith('_')]

    @property
    def __attrs_list(self):
        """
        Compose a list with all the possibles attributes

        :return: the list with attributes names
        """
        return self.__allowed_attrs['required'] + self.__allowed_attrs['arg_details'] + self.__allowed_attrs[
            'arg_relations']

    def __validate_args(self):
        """
        Check if the attributes are in valid attributes names list
        """
        from sys import exit

        if not set(self.__declared_attrs).issubset(self.__attrs_list):
            conflicts = ', '.join(list(set(self.__declared_attrs) - set(self.__attrs_list)))
            print('These parameters: {} are not valid'.format(conflicts))
            exit(0)

    def to_dict(self):
        """
        Parse the object to dict
        :return: the dict
        """
        dict_repr = {'arg_details': {}}
        for detail in self.__allowed_attrs['arg_details']:
            if hasattr(self, detail):
                dict_repr['arg_details'][detail] = getattr(self, detail)

        for relation in self.__allowed_attrs['arg_relations']:
            if hasattr(self, relation):
                dict_repr[relation] = getattr(self, relation)
        return dict_repr


def arg_to_attr(arg_name):
    """
    Format an argument like an object attribute

    :param arg: the list of arguments name to parse
    :return: the parsed attributes list
    """
    return [arg.replace('--', '').replace('-', '_') for arg in arg_name]


def attr_to_arg(attr):
    """
    Format an attributes like a CLI argument

    :param attr: the attribute to parse
    :return: the parsed argument
    """
    return '--{}'.format(attr.replace('_', '-'))
