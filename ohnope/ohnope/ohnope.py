"""
Functions and routines associated with rawberth Oh-nope IRC Services.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import TYPE_CHECKING

from encommon.times import Time
from encommon.types import DictStrAny
from encommon.types import clsname

from enrobie.clients import IRCClient
from enrobie.clients import IRCClientParams
from enrobie.plugins import AutoJoinPlugin
from enrobie.plugins import AutoJoinPluginParams
from enrobie.plugins import AutoNickPlugin
from enrobie.plugins import AutoNickPluginParams
from enrobie.plugins import StatusPlugin
from enrobie.plugins import StatusPluginParams
from enrobie.robie import Robie as _Robie
from enrobie.robie import RobieConfig
from enrobie.robie.addons import RobieLogger
from enrobie.robie.addons import RobieQueue
from enrobie.robie.childs import RobieClient
from enrobie.robie.models import RobieCommand

from ..plugins import ChanServ
from ..plugins import ChanServParams
from ..plugins import ChatServ
from ..plugins import ChatServParams
from ..plugins import HelpServ
from ..plugins import HelpServParams
from ..plugins import HostServ
from ..plugins import HostServParams
from ..plugins import MemoServ
from ..plugins import MemoServParams
from ..plugins import NickServ
from ..plugins import NickServParams
from ..plugins import OperServ
from ..plugins import OperServParams
from ..plugins import RootServ
from ..plugins import RootServParams
from ..plugins import StatServ
from ..plugins import StatServParams

if TYPE_CHECKING:
    from .config import OhnopeConfig
    from .params import OhnopeParams



class Robie(_Robie):
    """
    Interact with chat networks and integrate using plugins.

    :param config: Primary class instance for configuration.
    """

    __ohnope: 'Ohnope'


    def __init__(
        self,
        ohnope: 'Ohnope',
        config: RobieConfig,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        self.__ohnope = ohnope

        super().__init__(config)


    @property
    def ohnope(
        self,
    ) -> 'Ohnope':
        """
        Return the Ohnope instance to which the instance belongs.

        :returns: Ohnope instance to which the instance belongs.
        """

        return self.__ohnope



class Ohnope:
    """
    Interact with chat networks and integrate using plugins.

    :param config: Primary class instance for configuration.
    """

    __config: 'OhnopeConfig'

    __robie: Robie


    def __init__(  # noqa: CFQ001
        self,
        config: 'OhnopeConfig',
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        config.logger.log_d(
            base=clsname(self),
            status='initial')

        self.__config = config

        params = config.params


        peering = (
            config.params
            .peering)

        assert peering is not None

        dumped = peering.endumped

        if 'name' in dumped:

            dumped['servername'] = (
                dumped['name'])

            del dumped['name']

        if 'unique' in dumped:

            dumped['serverid'] = (
                dumped['unique'])

            del dumped['unique']

        if 'about' in dumped:

            dumped['realname'] = (
                dumped['about'])

            del dumped['about']

        if 'status' in dumped:
            del dumped['status']

        dumped['operate'] = 'service'

        source: DictStrAny = {
            'enable': True,
            'client': dumped,
            'status': peering.status}

        config.robie.register(
            name='ohnope',
            client=IRCClientParams,
            source=source)


        client = (
            config.params
            .client)

        assert client is not None

        dumped = client.endumped

        if 'status' in dumped:
            del dumped['status']

        source = {
            'enable': True,
            'client': dumped,
            'status': client.status}

        config.robie.register(
            name='eponho',
            client=IRCClientParams,
            source=source)


        channels = [
            {'channel': '#opers',
             'client': 'eponho'}]

        source = {
            'enable': bool(client),
            'channels': channels,
            'status': client.status}

        config.robie.register(
            name='autojoin',
            plugin=AutoJoinPluginParams,
            source=source)


        source = {
            'enable': bool(client),
            'clients': 'eponho',
            'status': client.status}

        config.robie.register(
            name='autonick',
            plugin=AutoNickPluginParams,
            source=source)


        status = (
            params.status
            .endumped)

        config.robie.register(
            name='status',
            plugin=StatusPluginParams,
            source=status)


        rootserv = (
            params.rootserv
            .endumped)

        config.robie.register(
            name='rootserv',
            plugin=RootServParams,
            source=rootserv)


        operserv = (
            params.operserv
            .endumped)

        config.robie.register(
            name='operserv',
            plugin=OperServParams,
            source=operserv)


        statserv = (
            params.statserv
            .endumped)

        config.robie.register(
            name='statserv',
            plugin=StatServParams,
            source=statserv)


        nickserv = (
            params.nickserv
            .endumped)

        config.robie.register(
            name='nickserv',
            plugin=NickServParams,
            source=nickserv)


        chanserv = (
            params.chanserv
            .endumped)

        config.robie.register(
            name='chanserv',
            plugin=ChanServParams,
            source=chanserv)


        memoserv = (
            params.memoserv
            .endumped)

        config.robie.register(
            name='memoserv',
            plugin=MemoServParams,
            source=memoserv)


        hostserv = (
            params.hostserv
            .endumped)

        config.robie.register(
            name='hostserv',
            plugin=HostServParams,
            source=hostserv)


        helpserv = (
            params.helpserv
            .endumped)

        config.robie.register(
            name='helpserv',
            plugin=HelpServParams,
            source=helpserv)


        chatserv = (
            params.chatserv
            .endumped)

        config.robie.register(
            name='chatserv',
            plugin=ChatServParams,
            source=chatserv)


        robie = config.robie

        self.__robie = (
            Robie(self, robie))


        self.robie.register(
            name='eponho',
            client=IRCClient)

        self.robie.register(
            name='ohnope',
            client=IRCClient)


        self.robie.register(
            name='autojoin',
            plugin=AutoJoinPlugin)

        self.robie.register(
            name='autonick',
            plugin=AutoNickPlugin)

        self.robie.register(
            name='status',
            plugin=StatusPlugin)


        self.robie.register(
            name='rootserv',
            plugin=RootServ)

        self.robie.register(
            name='operserv',
            plugin=OperServ)

        self.robie.register(
            name='statserv',
            plugin=StatServ)

        self.robie.register(
            name='nickserv',
            plugin=NickServ)

        self.robie.register(
            name='chanserv',
            plugin=ChanServ)

        self.robie.register(
            name='memoserv',
            plugin=MemoServ)

        self.robie.register(
            name='hostserv',
            plugin=HostServ)

        self.robie.register(
            name='helpserv',
            plugin=HelpServ)

        self.robie.register(
            name='chatserv',
            plugin=ChatServ)


        config.logger.log_d(
            base=clsname(self),
            status='created')


    @property
    def config(
        self,
    ) -> 'OhnopeConfig':
        """
        Return the Config instance containing the configuration.

        :returns: Config instance containing the configuration.
        """

        return self.__config


    @property
    def robie(
        self,
    ) -> Robie:
        """
        Return the Robie instance to which the instance belongs.

        :returns: Robie instance to which the instance belongs.
        """

        return self.__robie


    @property
    def logger(
        self,
    ) -> RobieLogger:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return self.robie.logger


    @property
    def params(
        self,
    ) -> 'OhnopeParams':
        """
        Return the Pydantic model containing the configuration.

        :returns: Pydantic model containing the configuration.
        """

        return self.config.params


    @property
    def client(
        self,
    ) -> RobieClient:
        """
        Return the value for the attribute from class instance.

        :returns: Value for the attribute from class instance.
        """

        return (
            self.robie
            .childs.clients
            ['ohnope'])


    @property
    def dumped(
        self,
    ) -> DictStrAny:
        """
        Return the facts about the attributes from the instance.

        :returns: Facts about the attributes from the instance.
        """

        return self.robie.dumped


    def register(
        self,
        cqueue: RobieQueue[RobieCommand],
        nickname: str,
        realname: str,
        unique: str,
    ) -> None:
        """
        Register the service as a client within the IRC network.

        :param cqueue: Queue instance where the item is received.
        :param nickname: Nickname that will be used for client.
        :param realname: Realname that will be used for client.
        :param unique: Unique identifer for the service client.
        """

        client = self.client

        assert isinstance(
            client, IRCClient)

        params = (
            self.params
            .peering)

        assert params is not None

        euqinu = params.unique

        client.put_command(
            cqueue,
            (f':{euqinu}'
             f' UID {nickname}'
             f' 0 {Time().spoch}'
             f' {nickname.lower()}'
             f' {params.name}'
             f' {euqinu}{unique}'
             f' 0 +Sio'
             f' {params.name}'
             f' {params.name}'
             f' * :{realname}'))
