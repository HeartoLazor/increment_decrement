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
