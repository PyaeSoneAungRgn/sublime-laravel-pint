import sublime
import sublime_plugin

class LaravelPintCommand(sublime_plugin.WindowCommand):
  def run(self):
    folder = self.window.folders()[0]
    self.window.run_command("exec", {
      "working_dir": folder,
      "cmd": [
        "./vendor/bin/pint"
      ]
    })

class LaravelPintCurrentFileCommand(sublime_plugin.WindowCommand):
  def run(self):
    folder = self.window.folders()[0]
    file = self.window.active_view().file_name()
    self.window.run_command("exec", {
      "working_dir": folder,
      "cmd": [
        "./vendor/bin/pint",
        file
      ]
    })

class LaravelPintTestCommand(sublime_plugin.WindowCommand):
  def run(self):
    folder = self.window.folders()[0]
    self.window.run_command("exec", {
      "working_dir": folder,
      "cmd": [
        "./vendor/bin/pint",
        "--test"
      ]
    })