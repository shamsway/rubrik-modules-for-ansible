# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BulkStatus(Model):
    """BulkStatus.

    :param statuses:
    :type statuses: list of :class:`IdStatus <rubriklib_int.models.IdStatus>`
    """

    _validation = {
        'statuses': {'required': True},
    }

    _attribute_map = {
        'statuses': {'key': 'statuses', 'type': '[IdStatus]'},
    }

    def __init__(self, statuses):
        self.statuses = statuses