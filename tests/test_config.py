from dmsapi.config import Config


def test_get_entrypoints():
    assert Config.entrypoints['ROOT'] == 'https://api.dms.istruly.sexy/'
