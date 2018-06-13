#Author: Hearto Lazor
#Sublime Text plugin to increment/decrement all selected numbers in text.
#Plugin page: https://github.com/HeartoLazor/increment_decrement
#Based in https://gist.github.com/dtao/2788978 from https://gist.github.com/dtao
#Installation:
#   Place the file under the Packages directory
#   For example: C:\Users<Username>\AppData\Roaming\Sublime Text 3\Packages\User.
#   In ST3: Preferences > Key Bindings Add this snippet with your chosen binding:
#      { "keys": ["ctrl+alt+a"], "command": "increment"},
#      { "keys": ["ctrl+alt+z"], "command": "decrement"}

import sublime
import sublime_plugin
import re

class NumberCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        for region in selection:
            text = self.view.substr(region)
            numbers = re.findall(r'[+-]?\d+', text)
            text = re.sub(r'[+-]?\d+', "%d", text)
            numbers_size = len(numbers)
            for i in range(0,numbers_size):
                try:
                    numbers[i] = self.op(int(numbers[i]))
                except ValueError:
                    return
            text = text % tuple(numbers)
            self.view.replace(edit, region, text)

    def is_enabled(self):
        return len(self.view.sel()) > 0

class IncrementCommand(NumberCommand):
    def op(self, value):
          return value + 1

class DecrementCommand(NumberCommand):
    def op(self, value):
          return value - 1
