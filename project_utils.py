import json
import yaml


class YamlConfig:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def loadYamlAsObject(file_name: str):
    with open(file_name, "r") as stream:
        str = json.dumps(yaml.safe_load(stream))
        loaded = json.loads(str, object_hook=lambda d: YamlConfig(**d))
        return loaded
