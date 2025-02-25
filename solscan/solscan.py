import json
from importlib import resources

import requests

import solscan
from solscan import configs
from solscan.enums.fields_enum import FieldsEnum as fields
from solscan.utils.parsing import ResponseParser as parser


class Solscan:
    def __new__(cls, api_key: str, net: str = "MAINNET"):
        with resources.path(configs, f"{net.upper()}-stable.json") as path:
            config_path = str(path)
        return cls.from_config(api_key=api_key, config_path=config_path, net=net)

    @staticmethod
    def __load_config(config_path: str) -> dict:
        with open(config_path, "r") as f:
            return json.load(f)

    @staticmethod
    def __run(func, api_key: str, net: str):
        def wrapper(*args, **kwargs):
            url = (
                f"{fields.PREFIX.format(net.lower()).replace('-mainnet','')}"
                f"{func(*args, **kwargs)}"
                f"{fields.API_KEY}"
                f"{api_key}"
            )
            r = requests.get(url, headers={"User-Agent": ""})
            return parser.parse(r)

        return wrapper

    @classmethod
    def from_config(cls, api_key: str, config_path: str, net: str):
        config = cls.__load_config(config_path)
        for func, v in config.items():
            if not func.startswith("_"):  # disabled if _
                attr = getattr(getattr(solscan, v["module"]), func)
                setattr(cls, func, cls.__run(attr, api_key, net))
        return cls
