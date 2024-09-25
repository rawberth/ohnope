"""
Functions and routines associated with rawberth Oh-nope IRC Services.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from encommon.types import NCNone

from enrobie.clients.irc.message import IRCMessage
from enrobie.plugins import StatusPlugin
from enrobie.plugins import StatusPluginStates
from enrobie.robie.childs import RobiePlugin
from enrobie.robie.threads import RobieThread

from .params import MemoServParams



class MemoServ(RobiePlugin):
    """
    Integrate with the Robie routine and perform operations.
    """


    def __post__(
        self,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        self.__status('normal')


    def validate(
        self,
    ) -> None:
        """
        Perform advanced validation on the parameters provided.
        """

        # Review the parameters


    def operate(
        self,
        thread: RobieThread,
    ) -> None:
        """
        Perform the operation related to Homie service threads.

        :param thread: Child class instance for Chatting Robie.
        """

        from ...ohnope import Robie

        assert isinstance(
            thread.robie, Robie)

        robie = thread.robie

        ohnope = robie.ohnope
        member = thread.member
        mqueue = thread.mqueue
        params = self.params

        assert isinstance(
            params, MemoServParams)

        while not mqueue.empty:

            mitem = mqueue.get()

            assert isinstance(
                mitem, IRCMessage)

            event = (
                mitem.event
                .original)

            if event[:8] == 'NETINFO ':

                ohnope.register(
                    member.cqueue,
                    params.nickname,
                    params.realname,
                    params.unique)


    def __status(
        self,
        status: StatusPluginStates,
    ) -> None:
        """
        Update or insert the status of the Robie child instance.

        :param status: One of several possible value for status.
        """

        robie = self.robie
        childs = robie.childs
        plugins = childs.plugins
        params = self.params

        assert isinstance(
            params,
            MemoServParams)

        if 'status' not in plugins:
            return NCNone

        plugin = plugins['status']

        assert isinstance(
            plugin,
            StatusPlugin)

        (plugin.update(
            unique=self.name,
            group='Services',
            title='Service',
            icon=params.status,
            state=status))
