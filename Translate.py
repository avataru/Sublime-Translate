# -*- coding: utf-8 -*-

import sublime, sublime_plugin
import os, re

settings = sublime.load_settings('Translate.sublime-settings')

# Menu (re)builder based on the settings

class TranslateMenu:
	def build(self, menu):
		menu_file_path = os.path.join(sublime.packages_path(), 'Sublime-Translate', menu + '.sublime-menu')

		translation_maps = settings.get('maps').keys()
		translation_maps = sorted(translation_maps,
		    key=lambda s: s.lower())

		menu_regex = re.compile(r'"id"\s*:\s*"translation_maps"\s*,\s*"children"\s*:\s*(\[[^[]*?])', re.I | re.M | re.S)
		menu_file = open(menu_file_path, 'r')
		menu_data = menu_file.read()
		menu_file.close()

		menu_indentation = re.search(r'\n(\s*)"id"\s*:\s*"translation_maps"', menu_data , re.I | re.M | re.S).group(1)

		updated_menu_items = '"id": "translation_maps",\n' + menu_indentation  + '"children": \n' + menu_indentation + '[\n'

		for map_id in translation_maps:
			updated_menu_items += menu_indentation + '\t{\n'
			updated_menu_items += menu_indentation + '\t\t"caption": "' + settings.get('maps')[map_id]['name'] + '",\n'
			updated_menu_items += menu_indentation + '\t\t"command": "translate_map", "args": { "character_set": "' + map_id + '"}\n'
			updated_menu_items += menu_indentation + '\t}'
			updated_menu_items += ',\n'
		updated_menu_items = updated_menu_items[:-2] + '\n'
		updated_menu_items += menu_indentation + ']'
		updated_menu_data = menu_regex.sub(updated_menu_items, menu_data)

		menu_file = open(menu_file_path, 'w')
		menu_file.write(updated_menu_data)
		menu_file.close()

	def rebuild(self):
		self.build('Main')
		self.build('Context')

TranslateMenu().rebuild()

settings.clear_on_change('maps')
settings.add_on_change('maps', lambda:TranslateMenu().rebuild())

# The plugin

class TranslateMapCommand(sublime_plugin.TextCommand):
	def run(self, edit, character_set):
		character_map = settings.get('maps')[character_set]['map']

		for selection in self.view.sel():
			parsed_text = replace_from_list(character_map, self.view.substr(selection))
			self.view.replace(edit, selection, unicode(parsed_text, 'utf-8'))

	def is_enabled(self):
		return self.view.sel()[0].size()

def replace_from_list(replacements, string):
	parsed_string = u''

	for character in string:
		if character.encode('utf-8') in replacements.keys():
			parsed_string += replacements[character.encode('utf-8')]
		else:
			parsed_string += character
	return parsed_string.encode('utf-8')