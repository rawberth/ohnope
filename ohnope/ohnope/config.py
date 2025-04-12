"""
Functions and routines associated with rawberth Oh-nope IRC Services.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Optional

from encommon.config import Config
from encommon.config import Params
from encommon.types import DictStrAny
from encommon.utils.common import PATHABLE

from enrobie.robie import RobieConfig

from .params import OhnopeParams



class OhnopeConfig(Config):
    """
    Contain the configurations from the arguments and files.

    :param sargs: Additional arguments on the command line.
    :param files: Complete or relative path to config files.
    :param cargs: Configuration arguments in dictionary form,
        which will override contents from the config files.
    """

    __robie: RobieConfig


    def __init__(
        self,
        sargs: Optional[DictStrAny] = None,
        files: Optional[PATHABLE] = None,
        cargs: Optional[DictStrAny] = None,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        sargs = dict(sargs or {})
        cargs = dict(cargs or {})


        _console = (
            sargs.get('console'))

        _debug = (
            sargs.get('debug'))

        key = 'enlogger/stdo_level'

        if _console is True:
            cargs[key] = 'info'

        if _debug is True:
            cargs[key] = 'debug'


        if 'config' in sargs:
            files = sargs['config']

            del sargs['config']


        super().__init__(
            files=files,
            cargs=cargs,
            sargs=sargs,
            model=OhnopeParams)

        self.merge_params()


        insert: DictStrAny = {}

        persons = (
            self.params
            .endumped['persons'])

        if persons is not None:
            insert = {'persons': persons}


        config = RobieConfig(
            cargs=self.cargs | insert,
            sargs=self.sargs)

        setattr(
            config,
            '_Config__logger',
            self.logger)

        setattr(
            config,
            '_Config__crypts',
            self.crypts)

        self.__robie = config


    @property
    def params(
        self,
    ) -> OhnopeParams:
        """
        Return the Pydantic model containing the configuration.

        .. warning::
           This method completely overrides the parent but is
           based on that code, would be unfortunate if upstream
           changes meant this breaks or breaks something else.

        :returns: Pydantic model containing the configuration.
        """

        params = self.__params

        if params is not None:

            assert isinstance(
                params, OhnopeParams)

            return params


        basic = self.basic

        params = (
            self.model(**basic))

        assert isinstance(
            params, OhnopeParams)


        self.__params = params

        return self.__params


    def merge_params(
        self,
    ) -> None:
        """
        Update the Pydantic model containing the configuration.
        """

        merge = self.merge
        jinja2 = self.jinja2

        jinja2.set_static(
            'source', merge)

        parse = jinja2.parse

        params = self.model(
            parse, **merge)

        assert isinstance(
            params, OhnopeParams)

        (jinja2
         .set_static('source'))

        self.__params = params


    @property
    def __params(
        self,
    ) -> Optional[Params]:
        """
        Return the Pydantic model containing the configuration.

        :returns: Pydantic model containing the configuration.
        """

        return self._Config__params


    @__params.setter
    def __params(
        self,
        value: Params,
    ) -> None:
        """
        Update the value for the attribute from class instance.
        """

        self._Config__params = value


    @property
    def robie(
        self,
    ) -> RobieConfig:
        """
        Return the Config instance containing the configuration.

        :returns: Config instance containing the configuration.
        """

        return self.__robie
