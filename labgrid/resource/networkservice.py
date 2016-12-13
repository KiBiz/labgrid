import attr
from .resource import InfoResource


@attr.s
class NetworkService(InfoResource):
    addresses = attr.ib(default={},
                        validator=attr.validators.instance_of(dict))
    hostname = attr.ib(default="", validator=attr.validators.instance_of(str))

    def get_if_addr(self, adr):
        """Returns the address for the specified interface"""
        return self.addresses[adr] #pylint: disable=unsubscriptable-object

    def get_hostname(self):
        """Returns the address for the specified interface"""
        return self.hostname #pylint: disable=unsubscriptable-object
