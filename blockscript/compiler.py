# Read in project.json, parse it, and store it in a variable called project.

import json

# import zipfile


def test_none():  # Satisfy pytest
    assert 0 == 0


def jprint(obj):
    print(json.dumps(obj, indent=4, sort_keys=True))


def jprint(title, obj):
    print(title + "\n")
    print(json.dumps(obj, indent=4, sort_keys=True))


def keyFromIndex(dict, n=0):
    if n < 0:
        n += len(dict)
    for A, B in enumerate(dict.keys()):
        if A == n:
            return B
    raise IndexError("dict index out of range")


def rep(str, A, B):
    return str.strip().replace(A, B)


def sbimport(project_name):
    # Read in project.json
    with open(project_name + "/project.json") as json_file:
        project = json.load(json_file)

    project_targets = project["targets"]
    stage = next((target for target in project_targets if target["isStage"]), None)
    sprites = [target for target in project_targets if not target["isStage"]]

    if stage is not None:
        variables = stage["variables"]
        lists = stage["lists"]
        sounds = stage["sounds"]

    # sprites.blocks.index

    script = open(project_name + ".bs3", "w")
    header = """Stage {
        // Global parameters and Stage properties go here

    }"""
    tab = "    "

    try:
        # Stage

        script.write("Stage {")
        script.write(f"\n{tab}// Global parameters and Stage properties go here")

        variables = stage["variables"]

        for i in range(len(variables)):
            variable = variables[keyFromIndex(variables, i)]
            variable[0] = rep(variable[0], " ", "_")

        for i in range(len(variables)):
            variable = variables[keyFromIndex(variables, i)]
            script.write(f"\n{tab}{variable[0]} = {variable[1]}")

        script.write("\n}")

        # Sprites

        script.write("\n\n// Sprites")
        for sprite in sprites:
            blocks = sprite["blocks"]

            script.write("\n\n")
            script.write(sprite["name"] + " {\n")

            # Blocks

            for i in range(len(blocks)):
                block = blocks[keyFromIndex(blocks, i)]
                script.write(tab + block["opcode"].split("_")[1] + "\n")

            script.write("}")

    finally:
        script.close()
