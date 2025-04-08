"""
Functions and routines associated with rawberth Oh-nope IRC Services.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from typing import Any

from enrobie.robie.params import RobiePersonParams



class OhnopePersonParams(RobiePersonParams, extra='forbid'):
    """
    Process and validate the Robie configuration parameters.
    """


    def __init__(
        self,
        /,
        **data: Any,
    ) -> None:
        """
        Initialize instance for class using provided parameters.
        """

        matches = data.get('matches')

        if matches is not None:

            for match in matches:
                match['client'] = 'eponho'

        super().__init__(**data)
