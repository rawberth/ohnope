"""
Functions and routines associated with rawberth Oh-nope IRC Services.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from pathlib import Path

from encommon.types import DictStrAny
from encommon.utils import save_text

from enconnect.fixtures import client_ircsock

from pytest import fixture

from . import PROJECT
from .ohnope import Ohnope
from .ohnope import OhnopeConfig



__all__ = [
    'client_ircsock']



def config_factory(
    tmp_path: Path,
) -> OhnopeConfig:
    """
    Construct the instance for use in the downstream tests.

    :param tmp_path: pytest object for temporal filesystem.
    :returns: Newly constructed instance of related class.
    """

    content = (
        f"""

        enconfig:
          paths:
            - {tmp_path}/homie

        enlogger:
          stdo_level: info

        database: >-
          sqlite:///{tmp_path}/db

        peering:
          server: localhost
          port: 6900

        client:
          server: localhost
          port: 6697

        persons:
          hubert:
            enable: true
            first: Hubert
            last: Farnsworth
            matches:
              - match: hubert!hubert@localhost

        status:
          enable: true

        """)

    config_path = (
        tmp_path / 'config.yml')

    save_text(
        config_path, content)

    sargs = {
        'config': config_path,
        'console': True,
        'debug': True}

    return OhnopeConfig(sargs)



@fixture
def config(
    tmp_path: Path,
) -> OhnopeConfig:
    """
    Construct the instance for use in the downstream tests.

    :param tmp_path: pytest object for temporal filesystem.
    :returns: Newly constructed instance of related class.
    """

    return config_factory(tmp_path)



@fixture
def replaces(
    tmp_path: Path,
) -> DictStrAny:
    """
    Return the complete mapping of what replaced in sample.

    :param tmp_path: pytest object for temporal filesystem.
    :returns: Complete mapping of what replaced in sample.
    """

    return {
        'PROJECT': PROJECT,
        'TMPPATH': tmp_path}



def ohnope_factory(
    config: OhnopeConfig,
) -> Ohnope:
    """
    Construct the instance for use in the downstream tests.

    :param config: Primary class instance for configuration.
    :returns: Newly constructed instance of related class.
    """

    ohnope = Ohnope(config)

    return ohnope



@fixture
def ohnope(
    config: OhnopeConfig,
) -> Ohnope:
    """
    Construct the instance for use in the downstream tests.

    :param config: Primary class instance for configuration.
    :returns: Newly constructed instance of related class.
    """

    return ohnope_factory(config)
