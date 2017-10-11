# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class HostShareCredentialDetail(Model):
    """HostShareCredentialDetail.

    :param host_id:
    :type host_id: str
    :param username:
    :type username: str
    :param domain:
    :type domain: str
    """

    _validation = {
        'host_id': {'required': True},
        'username': {'required': True},
    }

    _attribute_map = {
        'host_id': {'key': 'hostId', 'type': 'str'},
        'username': {'key': 'username', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
    }

    def __init__(self, host_id, username, domain=None):
        self.host_id = host_id
        self.username = username
        self.domain = domain