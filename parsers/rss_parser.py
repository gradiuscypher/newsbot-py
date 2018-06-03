name = 'rss_parser.py'


def parse(*args, **kwargs):
    config = kwargs['config']
    actions = kwargs['actions']

    for action in actions:
        print("I'm RSS parser taking an action: {}".format(action.name))
        action.action()
