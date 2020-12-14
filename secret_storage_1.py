from typing import Any, Dict


class Storage:
    def __init__(self, data: Dict[str, Any]):
        self._data = data
        self._reserve_data = {
            "potato": 100,
        }
        self.__secret_data = {
            "supplier": "johnny",
        }

    def __getitem__(self, key):
        if key in self._data:
            return self._data[key]
        elif key in self._reserve_data:
            return self._reserve_data[key]
        else:
            raise KeyError("No key \"" + str(key) + "\" in actual or reserved data")


