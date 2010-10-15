# -*- coding: utf-8 -*-


from tipfy import Rule

def get_rules(app):

    rules = [
        Rule('/', endpoint='index', handler='apps.www.handlers.IndexHandler'),
        Rule('/debtors', endpoint='debtors', handler='apps.www.handlers.DebtorsHandler'),
        Rule('/accounts', endpoint='accounts', handler='apps.www.handlers.AccountsHandler'),
        Rule('/cssgen/icons', endpoint='cssicons', handler='apps.www.handlers.CssIconsHandler'),
    ]
    return rules
