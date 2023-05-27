# `./blockscript/opcodes`

`opcodes.json` is formatted like so:

```json
{
    "opcode": [
        {
            "name": ["name", "alternate name" ...],
            "type": "category",
            "tabs": int,
            "arguments": [arg1, arg2 ...],
            "follow": " follow",
            "end": " end"
        }
    ]
    ...
}
```

which becomes

```js
name (arg1, arg2) follow end
```

> **Note: opcodes are currently not being worked on. I am currently focusing on decoding the block orders and nesting at the moment**
