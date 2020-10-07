from src.IdentifierManager import IdentifierManager


def test_init():
    id_manager = IdentifierManager()
    assert len(id_manager.counts) > 0


def get_id():
    id_manager = IdentifierManager()

    identifier = id_manager.get_id('Program')
    assert identifier == 'provone#Program/1'
    assert 0


def test_get_property_id():
    id_manager = IdentifierManager()

    identifier = id_manager.get_id('fileName')
    assert identifier == 'sdtl#fileName'
    assert 0