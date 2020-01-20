# logicparser

A free layer to create logics for your arguments

## Getting Started

logicparser is a python package that allow you to create logic and dependncies
between CLI arguments.
These instructions will install logicparser to your machine.

### Prerequisites

* Python3
* PIP3

### Installation

```
pip3 install logicparser 
```

## Usage

### Define arguments

The class used to create a new argument is imported in this way:
```
from logicparser import Argument

arg = Argument(arg_name='--arg-name')
```

#### metavar

```
arg = Argument(arg_name='--arg-name', metavar='ARG_VALUE')
```

#### action 

```
arg = Argument(arg_name='--arg-name', action='store_true')
```

#### help 

```
arg = Argument(arg_name='--arg-name', help='This message will be show when you will define -h arg')
```

### Add relationships

#### require
You can define that an argument can be defined only if others arguments
are defined previously
```
arg = Argument(
    arg_name='arg-name',
    require=('--other-arg',))
```

#### conflict
You can define that an argument cannot be defined if other arguments are
defined previously
```
arg = Argument(
    arg_name='arg-name',
    conflict=('--other-arg',))
```

#### dependency
You can define that an arguments can be defined only if at least one of others
arguments is defined
```
arg = Argument(
    arg_name='arg-name',
    dependency=('--other-arg1', 'other-arg2',))
```

### Parse arguments
When you have defined the list of your arguments you can play 
args validation parsing them.
```
from logicparser import Argument, ArgumentHandler

args = ArgumentHandler([
    Argument(arg_name='--arg-name', ...),
    Argument(arg_name='--arg-name2', ...),
    Argument(arg_name='--arg-name3', ...),
    ...
]).args
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License, read [LICENSE](LICENSE) for details 

## Author

* **Giuseppe "mastrobirraio" Matranga** - *Initial work* - [Github](https://github.com/mastrobirraio)