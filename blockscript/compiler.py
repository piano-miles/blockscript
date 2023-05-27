import json
import time

# import zipfile # used to unzip sb3

with open("blockscript/opcodes/opcodes.json") as json_file:
    opcode = json.load(json_file)


def test_none():  # Satisfy pytest
    assert True


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


def write(script, x):
    # script.write(x)
    # print(x)
    # time.sleep(0.5)
    pass


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

        write(script, "Stage {")
        write(script, f"\n{tab}// Global parameters and Stage properties go here")

        variables = stage["variables"]

        for i in range(len(variables)):
            variable = variables[keyFromIndex(variables, i)]
            variable[0] = rep(variable[0], " ", "_")

        for i in range(len(variables)):
            variable = variables[keyFromIndex(variables, i)]
            write(script, f"\n{tab}{variable[0]} = {variable[1]}")

        write(script, "\n}")

        # Sprites

        write(script, "\n\n// Sprites")
        for sprite in sprites:
            blocks = sprite["blocks"]

            write(script, "\n\n")
            write(script, sprite["name"] + " {\n")

            # Blocks

            # Tabbing determines how many tabs to add to the start of each line
            tabbing = 1

            while len(blocks) > 0:
                nextBlock = "n/a"
                id = keyFromIndex(blocks, 0)  # Get the first block in the list

                # Abstract Syntax Tree (at least I think, I don't know mcuh about this stuff)
                AST = []
                ASTprop = []  # AST properties

                # The basic structure of the AST
                for block in blocks:
                    # If block is top level (thus forth referenced as TL)
                    if blocks[block]["topLevel"]:
                        # print(f"blocks:{json.dumps(blocks, indent=4, sort_keys=False)}")
                        AST.append([{block: blocks[block]}, []])  # Parent nodes of AST
                        ASTprop.append([{"tab": 1}, []])

                # print(f"*** AST: {json.dumps(AST, indent=4, sort_keys=False)}")

                ASTparents = AST

                # Loop through the next blocks for each TL block until there are no more (blocks going consecutively after each other)
                for i in range(len(ASTparents)):
                    ((j, v),) = ASTparents[i][0].items()  # j = TL block index
                    while nextBlock is not None:  # While there is a next block
                        nextBlock = blocks[j]["next"]  # Get the next block
                        parent = blocks[j]["parent"]  # Get the block's parent
                        block = blocks[j]["opcode"]  # Get the block's opcode

                        # opcode stuff
                        name = opcode[block][0]["name"][0]
                        type = opcode[block][0]["type"]
                        tabs = opcode[block][0]["tabs"]
                        arguments = opcode[block][0]["arguments"]
                        follow = opcode[block][0]["follow"]
                        end = opcode[block][0]["end"]

                        AST[i][1].append(blocks[j])  # Add block to branch
                        ASTprop[i][1].append({"tab": ASTprop[i][0]["tab"] + 1})

                        del blocks[j]  # Delete the block
                        j = nextBlock

                # Now search for loose parents

                # Write to file
                write(script, json.dumps(AST, indent=4, sort_keys=False))

            write(script, "}")

    finally:
        script.close()
