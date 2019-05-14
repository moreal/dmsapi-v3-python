from dmsapi import config


def test_get_entrypoints():
    assert config.entrypoints['ROOT'] == 'https://api.dms.istruly.sexy'
