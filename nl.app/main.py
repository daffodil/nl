# -*- coding: utf-8 -*-

import os
import sys

if 'lib' not in sys.path:
    # Add /lib as primary libraries directory, with fallback to /distlib
    # and optionally to distlib loaded using zipimport.
    sys.path[0:0] = ['lib', 'distlib', 'distlib.zip']

import config
import tipfy

# Is this the development server?
debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

# Instantiate the application.
app = tipfy.make_wsgi_app(config=config.config, debug=debug)


def main():
    app.run()


if __name__ == '__main__':
    main()
