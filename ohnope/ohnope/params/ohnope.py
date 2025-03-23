"""
Functions and routines associated with rawberth Oh-nope IRC Services.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated
from typing import Any
from typing import Callable
from typing import Optional

from encommon.config import Params

from enrobie.plugins import StatusPluginIconParams
from enrobie.plugins import StatusPluginParams
from enrobie.robie.params import RobieParamsModel
from enrobie.robie.params import RobiePrinterParams
from enrobie.robie.params import RobieServiceParams

from pydantic import Field

from ...plugins import ChanServParams
from ...plugins import ChatServParams
from ...plugins import HelpServParams
from ...plugins import HostServParams
from ...plugins import MemoServParams
from ...plugins import NickServParams
from ...plugins import OperServParams
from ...plugins import RootServParams
from ...plugins import StatServParams



class OhnopeIRCParams(RobieParamsModel, extra='forbid'):
    """
    Process and validate the core configuration parameters.
    """

    server: Annotated[
        str,
        Field(...,
              description='Server address for connection',
              min_length=1)]

    port: Annotated[
        int,
        Field(6900,
              description='Server address for connection',
              ge=1, le=65535)]

    timeout: Annotated[
        int,
        Field(30,
              description='Timeout connecting to server',
              ge=1, le=300)]

    nickname: Annotated[
        str,
        Field('ohnope',
              description='Parameter for the integration',
              min_length=1)]

    username: Annotated[
        str,
        Field('ohnope',
              description='Parameter for the integration',
              min_length=1)]

    realname: Annotated[
        str,
        Field('Oh-nope IRC Services',
              description='Parameter for the integration',
              min_length=1)]

    channel: Annotated[
        str,
        Field('#opers',
              description='Channel where client will join',
              min_length=1)]

    ssl_enable: Annotated[
        bool,
        Field(True,
              description='Enable connection encryption')]

    ssl_verify: Annotated[
        bool,
        Field(True,
              description='Verify the ceritifcate valid')]

    status: Annotated[
        StatusPluginIconParams,
        Field(default_factory=StatusPluginIconParams,
              description='Icon used per chat platform')]



class OhnopeIRCSParams(RobieParamsModel, extra='forbid'):
    """
    Process and validate the core configuration parameters.
    """

    server: Annotated[
        str,
        Field(...,
              description='Server address for connection',
              min_length=1)]

    port: Annotated[
        int,
        Field(6900,
              description='Server address for connection',
              ge=1, le=65535)]

    timeout: Annotated[
        int,
        Field(30,
              description='Timeout connecting to server',
              ge=1, le=300)]

    password: Annotated[
        Optional[str],
        Field(None,
              description='Parameter for the integration',
              min_length=1)]

    name: Annotated[
        str,
        Field('services.invalid',
              description='Parameter for the integration',
              min_length=1)]

    unique: Annotated[
        str,
        Field('42X',
              description='Unique identifier for services',
              min_length=1)]

    about: Annotated[
        str,
        Field('Chatting Robie',
              description='Parameter for the integration',
              min_length=1)]

    ssl_enable: Annotated[
        bool,
        Field(True,
              description='Enable connection encryption')]

    ssl_verify: Annotated[
        bool,
        Field(True,
              description='Verify the ceritifcate valid')]

    status: Annotated[
        StatusPluginIconParams,
        Field(default_factory=StatusPluginIconParams,
              description='Icon used per chat platform')]



class OhnopeParams(Params, extra='forbid'):
    """
    Process and validate the core configuration parameters.
    """

    database: Annotated[
        str,
        Field('sqlite:///:memory:',
              description='Database connection string',
              min_length=1)]

    printer: Annotated[
        RobiePrinterParams,
        Field(default_factory=RobiePrinterParams,
              description='Print messages to console')]

    service: Annotated[
        RobieServiceParams,
        Field(default_factory=RobieServiceParams,
              description='Parameters for Robie Service')]

    peering: Annotated[
        Optional[OhnopeIRCSParams],
        Field(None,
              description='Server connection parameters')]

    client: Annotated[
        Optional[OhnopeIRCParams],
        Field(None,
              description='Server connection parameters')]

    status: Annotated[
        StatusPluginParams,
        Field(default_factory=StatusPluginParams,
              description='Parameters for the plugin')]

    rootserv: Annotated[
        RootServParams,
        Field(default_factory=RootServParams,
              description='Parameters for the plugin')]

    operserv: Annotated[
        OperServParams,
        Field(default_factory=OperServParams,
              description='Parameters for the plugin')]

    statserv: Annotated[
        StatServParams,
        Field(default_factory=StatServParams,
              description='Parameters for the plugin')]

    nickserv: Annotated[
        NickServParams,
        Field(default_factory=NickServParams,
              description='Parameters for the plugin')]

    chanserv: Annotated[
        ChanServParams,
        Field(default_factory=ChanServParams,
              description='Parameters for the plugin')]

    memoserv: Annotated[
        MemoServParams,
        Field(default_factory=MemoServParams,
              description='Parameters for the plugin')]

    hostserv: Annotated[
        HostServParams,
        Field(default_factory=HostServParams,
              description='Parameters for the plugin')]

    helpserv: Annotated[
        HelpServParams,
        Field(default_factory=HelpServParams,
              description='Parameters for the plugin')]

    chatserv: Annotated[
        ChatServParams,
        Field(default_factory=ChatServParams,
              description='Parameters for the plugin')]


    def __init__(
        # NOCVR
        self,
        /,
        _parse: Optional[Callable[..., Any]] = None,
        **data: Any,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """


        if _parse is not None:

            parsable = [
                'database',
                'printer',
                'service',
                'peering']

            for key in parsable:

                value = data.get(key)

                if value is None:
                    continue

                value = _parse(value)

                data[key] = value


        super().__init__(**data)
