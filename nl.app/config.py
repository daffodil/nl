# -*- coding: utf-8 -*-
"""
    Configuration settings.
"""
config = {}


config['tipfy'] = {
    # Enable debugger. It will be loaded only in development.
    'middleware': [
        'tipfy.ext.debugger.DebuggerMiddleware',
    ],
    
    # apps
    'apps_installed': [
         'apps.www',
         'apps.ajax'
    ],
}
