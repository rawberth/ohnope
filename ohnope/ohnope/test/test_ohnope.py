"""
Functions and routines associated with rawberth Oh-nope IRC Services.

This file is part of Enasis Network software eco-system. Distribution
is permitted, for more information consult the project license file.
"""



from encommon.types import DictStrAny
from encommon.types import inrepr
from encommon.types import instr
from encommon.types import lattrs
from encommon.utils import load_sample
from encommon.utils import prep_sample
from encommon.utils.sample import ENPYRWS

from . import SAMPLES
from ..ohnope import Ohnope



def test_Ohnope(
    ohnope: Ohnope,
    replaces: DictStrAny,
) -> None:
    """
    Perform various tests associated with relevant routines.

    :param ohnope: Primary class instance of project parent.
    :param replaces: Mapping of what to replace in samples.
    """


    attrs = lattrs(ohnope)

    assert attrs == [
        '_Ohnope__config',
        '_Ohnope__robie']


    assert inrepr(
        'ohnope.Ohnope',
        ohnope)

    assert isinstance(
        hash(ohnope), int)

    assert instr(
        'ohnope.Ohnope',
        ohnope)


    assert ohnope.config

    assert ohnope.robie

    assert ohnope.logger

    assert ohnope.params

    assert ohnope.client


    assert ohnope is (
        ohnope.robie.ohnope)


    sample_path = (
        SAMPLES / 'dumped.json')

    sample = load_sample(
        path=sample_path,
        update=ENPYRWS,
        content=ohnope.dumped,
        replace=replaces)

    expect = prep_sample(
        content=ohnope.dumped,
        replace=replaces)

    assert expect == sample
