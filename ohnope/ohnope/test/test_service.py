"""
Functions and routines associated with rawberth Oh-nope IRC Services.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from threading import Thread
from time import sleep as block_sleep

from enconnect.fixtures import IRCClientSocket
from enconnect.irc.test import SVENTS

from enrobie.robie import RobieService

from ..ohnope import Ohnope



def test_RobieService(
    ohnope: Ohnope,
    client_ircsock: IRCClientSocket,
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param ohnope: Primary class instance of project parent.
    :param client_ircsock: Object to mock client connection.
    """

    robie = ohnope.robie

    service = RobieService(robie)

    client_ircsock(SVENTS)

    service.start()


    thread = Thread(
        target=service.operate)

    thread.start()


    block_sleep(10)

    assert service.running

    service.soft()

    while service.running:
        block_sleep(1)

    service.stop()

    thread.join()

    assert service.zombies
