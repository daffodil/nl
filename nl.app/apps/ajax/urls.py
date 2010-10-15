# -*- coding: utf-8 -*-


from tipfy import Rule

def get_rules(app):


    rules = [
       
       
        ##  Abbrevs
        Rule('/ajax/ags4/abbrevs',  endpoint='/ajax/ags4/abbrevs',
													handler='apps.ajax.handlers.AbbrevsAjaxHandler'),	
 
    ]

    return rules
