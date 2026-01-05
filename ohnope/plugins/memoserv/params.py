"""
Functions and routines associated with rawberth Oh-nope IRC Services.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Annotated
from typing import Any
from typing import Callable
from typing import Optional

from enrobie.plugins import StatusPluginIconParams
from enrobie.robie.params import RobiePluginParams

from pydantic import Field



class MemoServParams(RobiePluginParams, extra='forbid'):
    """
    Process and validate the core configuration parameters.
    """

    enable: Annotated[
        bool,
        Field(True,
              description='Determine if service enabled')]

    nickname: Annotated[
        str,
        Field('MemoServ',
              description='What nickname for the service',
              min_length=1)]

    realname: Annotated[
        str,
        Field('Offline message sharing',
              description='What realname for the service',
              min_length=1)]

    unique: Annotated[
        str,
        Field('MEMOS0',
              description='Unique identifier for service',
              min_length=1)]

    status: Annotated[
        StatusPluginIconParams,
        Field(default_factory=StatusPluginIconParams,
              description='Icon used per chat platform')]


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
                'nickname',
                'realname',
                'unique',
                'status']

            for key in parsable:

                value = data.get(key)

                if value is None:
                    continue

                value = _parse(value)

                data[key] = value


        super().__init__(
            _parse=_parse,
            **data)
