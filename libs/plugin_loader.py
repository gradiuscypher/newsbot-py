import os
import json
import logging
import traceback
from importlib import import_module


class PluginLoader:
    def __init__(self):
        self.logger = logging.getLogger('newsbot.py')
        self.actions = []
        self.parsers = []
        self.action_dir = 'actions'
        self.parser_dir = 'parsers'
        self.config = None
        self.action_config = None
        self.parser_config = None

    def load_plugins(self, config):
        self.config = config
        self.action_config = json.loads(self.config.get('newsbot', 'action_plugins'))
        self.parser_config = json.loads(self.config.get('newsbot', 'parser_plugins'))

        # Load the action plugins
        try:
            count = 0
            for plugin in self.action_config:
                plugin_file = plugin + '.py'
                location = os.path.join(self.action_dir, plugin_file)

                if not os.path.isdir(location):
                    self.actions.append(import_module(self.action_dir + '.' + plugin))
                    count += 1
            self.logger.info("Loaded {} actions.".format(count))

        except:
            self.logger.error(traceback.format_exc())

        # Load the parser plugins
        try:
            count = 0
            for plugin in self.parser_config:
                plugin_file = plugin + '.py'
                location = os.path.join(self.parser_dir, plugin_file)

                if not os.path.isdir(location):
                    self.parsers.append(import_module(self.parser_dir + '.' + plugin))
                    count += 1
            self.logger.info("Loaded {} parsers.".format(count))

        except:
            self.logger.error(traceback.format_exc())
