# Increment Decrement Sublime Plugin
Sublime Text plugin to increment/decrement all selected numbers in text.
https://gfycat.com/SeveralPointedHapuku

## Installation
Place the file under the Packages directory 

For example: `C:\Users<Username>\AppData\Roaming\Sublime Text 3\Packages\User`.

In ST3: Preferences > Key Bindings
Add this snippet with your chosen binding:
```
{ "keys": ["ctrl+alt+a"], "command": "increment"},
{ "keys": ["ctrl+alt+z"], "command": "decrement"}
```

## license
CC-0
Based in https://gist.github.com/dtao/2788978 from https://gist.github.com/dtao

Main Differences:
* Increment/Decrement ALL integers in text selection.
* Negative integer support.
