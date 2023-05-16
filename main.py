# Read in project.json, parse it, and store it in a variable called project.

import json


def jprint(obj):  # type: ignore
    print(json.dumps(obj, indent=4, sort_keys=True))


def jprint(title, obj):
    print(title+'\n')
    print(json.dumps(obj, indent=4, sort_keys=True))


project_name = "project"

# Read in project.json
with open(project_name + '/project.json') as json_file:
    project = json.load(json_file)

project_targets = project["targets"]
stage = next((target for target in project_targets if target["isStage"]), None)
project_targets = [
    target for target in project_targets if not target["isStage"]]

if stage is not None:
    variables = stage["variables"]
    lists = stage["lists"]
    sounds = stage["sounds"]
