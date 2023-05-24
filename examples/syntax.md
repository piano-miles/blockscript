# Blockscript Syntax

## NOTES

- Every ellipses in the following example (`...`) represents a placeholder for unelaborated code. Do not actually use ellipses in your code.
- Every time I use the word "`brace`", I am referring to the curly bracket character: `{` or `}`.

## GENERAL RULES

- All indents, groups of more than one space, and new lines are optional but reccomended for readibility.
- Semicolon delimeter.
- Every comment (starting with `//`) is optional. Comments are used to explain code.
- Multiline comments start with `/*` and end with `*/`.

## Syntax

```js
// The setup class is used to initialize variables and link assets. This must be named as exactly "Setup", as shown.
Setup {
    volume = 100; // Initialize default variables
    sounds = ["path-to-file/sound1.wav", "path-to-file/sound2.mp3"]; // Link sounds.
    costumes = ["path-to-file/costume1.png", "path-to-file/costume2.svg"]; // Link costumes.
    ...

    // The "var" keyword creates a variable.
    // NOTE: variable IDs are auto-indexed for the sb3 project file.
    var a; // Declare a variable. Automatically initialized to 0 (double precision float) by default.
    var a, b, c; // Declare multiple variables.
    var a = 10;
    var b = 20;
    var c = 30; // Valid way to declare and initialize multiple variables.
    var a = 10,
        b = 20,
        c = 30; // Another valid way to declare and initialize multiple variables. (Remember that new lines are optional.)
    var a = 10,
        b, c; // Another valid way to declare and initialize multiple variables.

    // CAUTION
    var a = 2 * 3 + 4; // WARNING. No delcaring potentially unresolvable expressions in the Setup class. This will still compile because the expression is easily resolvable automatically by the compiler (to 10), but it is not recommended.
    var a, b = a; // INVALID. The right hand side of an assignment must be a constant.
    ...

    // The "list" keyword creates a list (array).
    // NOTE: list names must not match variable names.
    list a; // Declare a list. Automatically initialized as an empty list by default.
    list a = [1, "cat", "3"]; // Declare and initialize a list.

    // CAUTION
    list a = [2 * 3 + 4] // WARNING. No delcaring potentially unresolvable expressions in the Setup class. This will still compile because the expression is easily resolvable automatically by the compiler (to [10]), but it is not recommended.
    list a = 4; // INVALID. Cannot initialize a list with a non-list value.
    list a = [3, "cat", cat] // INVALID. Cannot initialize a list with an unresolved expression. Strings must be in quotes.
    list a = [[3, 4], [5, 6]] // INVALID. No multi-dimensional lists.
}

// Declare the stage.
Stage { ...(blocks)... }

// Declare a sprite.
Sprite_1 { // Underscores converted to spaces in the project.
    name = "Sprite 1 with a particular name"; // Optional way to override the sprite name.
    when green flag clicked { // Begin event
        a = 3; // No var keyword if a is already declared.
        var g = 5; // A global variable may be declared in a sprite, but it is not recommended.
        // ^^^ Use the Setup class instead to declare global variables.
        // ^^^ Global variables declared in a sprite are still accessible by other sprites.
        // ^^^ There are no local variables. This creates a variable for ALL sprites.

        repeat(a * 3 + 1) { // Uses PEMDAS to parse expressions.
            g = g * sqrt(a);
            // Example of a function call.
            move 10 steps; // Move keyword looks for either parentheses or a value and the steps keyword.
            move(10); // Equivalent to above.
            ... // Waiting for closed brace to terminate repeat block.
        } // Terminate repeat block.

        forever { // All methods are uncapitalized.
            penup();
            pen up; // Equivalent to above.
            move(45, 50);
            move to x: 45, y: 50; // Equivalent to above.

            // Valid if statement:
            if (condition) {
                doSomething();
                doSomethingElse();
            }
            // Another valid if statement:
            if (condition)
                doSomething(); // Only one block of code is allowed without braces.
            // Valid if-else statement:
            if (condition) {
                doSomething();
            } else {
                doSomethingElse();
            }
            // Developer note: if statement should expect parenthesis and thus parameters followed by a single line of blocks (ending with a semicolon) or braces (in which case, multiple lines of blocks are in the if statement until the closing brace).
            ...
        }

        say(a);
        say a; // Equivalent to above.
        say(a, 2);
        say a for 2 seconds; // Equivalent to above.
    } // End event

    // Below is a stray chunk of floating code.
    // This may be included in the project, but is useless.
    // The compiler will give the option whether to prune stray code.
    repeat(5) {
        // do stuff;
    }
} // End Sprite 1

Sprite_2 { ...(blocks)... } // Declare more sprites.
```
