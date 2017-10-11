# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MssqlMissedRecoverableRangeError(Model):
    """MssqlMissedRecoverableRangeError.

    :param time:
    :type time: datetime
    :param event_series_id:
    :type event_series_id: str
    :param event_message:
    :type event_message: str
    """

    _validation = {
        'time': {'required': True},
    }

    _attribute_map = {
        'time': {'key': 'time', 'type': 'iso-8601'},
        'event_series_id': {'key': 'eventSeriesId', 'type': 'str'},
        'event_message': {'key': 'eventMessage', 'type': 'str'},
    }

    def __init__(self, time, event_series_id=None, event_message=None):
        self.time = time
        self.event_series_id = event_series_id
        self.event_message = event_message