# `opcodes.json` format

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

becomes

```js
name (arg1, arg2) follow end
```
