# -*- coding: utf-8 -*-
"""DSM Network data."""


class SynoDSMNetwork(object):
    """Class containing Network data."""

    API_KEY = "SYNO.DSM.Network"

    def __init__(self, dsm):
        self._dsm = dsm
        self._data = {}

    def update(self):
        """Updates network data."""
        raw_data = self._dsm.get(self.API_KEY, "list")
        if raw_data:
            self._data = raw_data["data"]

    @property
    def dns(self):
        """DNS of the NAS."""
        return self._data.get("dns")

    @property
    def gateway(self):
        """Gateway of the NAS."""
        return self._data.get("gateway")

    @property
    def hostname(self):
        """Host name of the NAS."""
        return self._data.get("hostname")

    @property
    def interfaces(self):
        """Interfaces of the NAS."""
        return self._data.get("interfaces", [])

    def interface(self, eth_id):
        """Interface of the NAS."""
        for interface in self.interfaces:
            if interface["id"] == eth_id:
                return interface
        return None

    @property
    def macs(self):
        """MACs of the NAS."""
        macs = []
        for interface in self.interfaces:
            macs.append(interface["mac"])
        return macs

    @property
    def workgroup(self):
        """Workgroup of the NAS."""
        return self._data.get("workgroup")
