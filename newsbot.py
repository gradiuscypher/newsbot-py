#!/usr/bin/env python
import logging
import configparser
from libs.plugin_loader import PluginLoader

"""
Goal is to run through multiple news source parsers, and do something with the parsed information:
send to a discord webhook as a newspost, send to a webhook as something to investigate sharing (via twitter, etc)

iterate over every parser, take information and send it to an action plugin for each type of action:
* twitter
* discord channels
* etc
"""

# Setup Logging
logger = logging.getLogger('newsbot')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('newsbot.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)

# Setup ConfigParser
config = configparser.RawConfigParser()
config.read('config.conf')

plugins = PluginLoader()


if __name__ == '__main__':
    logger.info('Loading plugins ... ')
    plugins.load_plugins(config)
    logger.info('Finished loading plugins ... ')

    for plugin in plugins.parsers:
        plugin.parse(config=config, actions=plugins.actions)
