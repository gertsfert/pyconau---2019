# Goodby `print` statement, Hello Debugger!

## Benifits of using debuggers when programming in Python.

-   Why use debuggers
-   Workflow
-   Tools
-   `breakpoint()`

## Why use debuggers?

-   `print` does not give a lot of context
    -   I.e. JSON/APIs are a bit of a pain
-   Debugger is the right tool for the job

    -   Helps examine the state of a runninig program
    -   Can write new snippets of code
    -   Increases productivity

## What does debugging look like

```python
breakpoint() # instead of print(items)
```

-   An error was raised, and a Pdb prompt is shown in the terminal
-   This is an interactive console, and can write python expressonis on the current state
-   `> interact` drops into Python REPL
-   `> continue` allows the program to continue running

## But wait there is more!

"Fixing bugs in code is a process of confirming one-by-one that the things you beleive to be true, are actually true"

-   Use `ipdb` via `pip install ipdb`
-   `pudb` is a graphical CLI
-   `IDEs` -> VSCode + PyCharm are good ones

## Breakpoints!

-   A breakpoint is like a trap - stops the flow of execution in the program.
-   Python 3.7 has `breakpoint()`
    -   Set debugger of choice using an environment variable
    -   Can set a flag to skip breakpoints

## Debugger Fundamentals

nina.to/au19 for cheatsheet

## Ipython Demo

Can use an alias to jump into an iPython REPL insteam (check her website)

aka.ms.pyblog -- new feature for vscode, line by line debugging for notebooks
