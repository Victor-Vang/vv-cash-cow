import json
import yaml

class YamlConfig:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    # def teams_iterator(self):
    #     for team_abbreviation, team_data in self.__dict__.items():
    #         if team_abbreviation != "teams":
    #             yield team_abbreviation, team_data

    def teams_iterator(self):
        teams = {}
        for abbreviation, team_data in self.teams.items():
            team_data[abbreviation] = team_data
        return teams

# def loadYamlAsObject(file_name: str):
#     with open(file_name, "r") as stream:
#         loaded = yaml.safe_load(stream)
#         return YamlConfig(**loaded)

def loadYamlAsObject(file_name: str):
    with open(file_name, "r") as stream:
        str = json.dumps(yaml.safe_load(stream))
        loaded = json.loads(str, object_hook=lambda d: YamlConfig(**d))
        return loaded
