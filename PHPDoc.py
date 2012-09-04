# adjusted by Linus Metzler (www.linusmetzler.me)
# based on Stackoverflow Search Plugin by Eric Martel (emartel@gmail.com / www.ericmartel.com)

# available commands
#   php_documentation_open_selection
#   php_documentation_search_selection
#   php_documentation_search_from_input

import sublime
import sublime_plugin

import subprocess
import webbrowser

def SearchFor(text):
    url = 'http://php.net/manual-lookup.php?pattern=' + text.replace(' ','%20')
    webbrowser.open_new_tab(url)

def OpenPHPFunctionReference(text):
    url = 'http://php.net/' + text.replace(' ','%20')
    webbrowser.open_new_tab(url)

class PHPDocumentationOpenSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                selection = self.view.word(selection)

            text = self.view.substr(selection)
            OpenPHPFunctionReference(text)

class PHPDocumentationSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                selection = self.view.word(selection)

            text = self.view.substr(selection)            
            SearchFor(text)

class PHPDocumentationSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search PHP.net documentation for', '',
            self.on_done, self.on_change, self.on_cancel)
    def on_done(self, input):
        SearchFor(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass