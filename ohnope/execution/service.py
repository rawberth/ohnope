"""
Functions and routines associated with rawberth Oh-nope IRC Services.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from argparse import ArgumentParser
from signal import SIGHUP
from signal import SIGINT
from signal import SIGTERM
from signal import signal
from sys import argv as sys_argv
from typing import Optional

from encommon.types import DictStrAny

from enrobie.robie import RobieService

from ..ohnope import Ohnope
from ..ohnope import OhnopeConfig



def arguments(
    args: Optional[list[str]] = None,
) -> DictStrAny:
    """
    Construct arguments which are associated with the file.

    :param args: Override the source for the main arguments.
    :returns: Construct arguments from command line options.
    """

    parser = ArgumentParser()

    args = args or sys_argv[1:]


    parser.add_argument(
        '--config',
        required=True,
        help=(
            'complete or relative '
            'path to config file'))


    parser.add_argument(
        '--console',
        action='store_true',
        default=False,
        help=(
            'write log messages '
            'to standard output'))


    parser.add_argument(
        '--debug',
        action='store_true',
        default=False,
        help=(
            'increase logging level '
            'for standard output'))


    return vars(
        parser
        .parse_args(args))



def operation(
    # NOCVR
    ohnope: Ohnope,
) -> None:
    """
    Perform whatever operation is associated with the file.

    :param ohnope: Primary class instance of project parent.
    """

    robie = ohnope.robie

    service = RobieService(robie)

    service.start()

    signal(SIGINT, service.soft)
    signal(SIGTERM, service.soft)
    signal(SIGHUP, service.soft)

    service.operate()



def execution(
    # NOCVR
    args: Optional[list[str]] = None,
) -> None:
    """
    Perform whatever operation is associated with the file.

    :param args: Override the source for the main arguments.
    """

    config = OhnopeConfig(
        arguments(args))

    config.logger.start()

    (config.robie
     .logger.start())

    config.logger.log_i(
        base='execution/service',
        status='started')

    ohnope = Ohnope(config)

    operation(ohnope)

    config.logger.log_i(
        base='execution/service',
        status='stopped')

    config.logger.stop()



if __name__ == '__main__':
    execution()  # NOCVR
