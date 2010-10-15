# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Abbrev(db.Model):
	table 		= db.StringProperty(indexed=True)
	description = db.StringProperty()
	version		= db.StringProperty(required=True, indexed=True)
	
	def dic(self):
		return {
				'table': self.table, 
				'description': self.description, 
				'version': self.version		
				}

class AbbrevCode(db.Model):
	table 		= db.StringProperty(indexed=True)
	code 		= db.StringProperty(indexed=True)
	description = db.StringProperty()
	version		= db.StringProperty(required=True, indexed=True)
	date_added 	= db.DateProperty(indexed=True, required=False)
	added_by	= db.StringProperty()
	
	def dic(self):
		return {'code': self.code, 
				'table': self.table, 
				'description': self.description,
				'date_added': 'TODO', 
				'added_by': self.added_by
				}

class AgsFile(db.Model):
	file_name 		= db.StringProperty(indexed=True)
	contents 		= db.TextProperty()
	date_created 	= db.DateTimeProperty(auto_now_add=True)
	
	def dic(self):
		return {
			'date_created': 'TODO', 
			'file_name': self.file_name
		}
	


class Group(db.Model):
	cls 		= db.StringProperty(indexed=True)
	name 		= db.StringProperty(indexed=True)
	description = db.StringProperty()
	version		= db.StringProperty(indexed=True, required=True)
	def dic(self):
		return {'class': str(self.cls), 
				'name': str(self.name), 
				'description': str(self.description)
				}




class Heading(db.Model):
	group 		= db.StringProperty(indexed=True)
	sort_order 	= db.IntegerProperty(indexed=True)
	status 		= db.StringProperty()
	name	 	= db.StringProperty(indexed=True)
	unit 		= db.StringProperty()
	description	= db.StringProperty()
	example 	= db.StringProperty()
	data_type 	= db.StringProperty()
	#rev_date 	= db.DateProperty()
	version		= db.StringProperty(indexed=True, required=True)
	def dic(self):
		return {
				'group': str(self.group), 
				'status': str(self.status),
				'name': str(self.name), 
				'unit': str(self.unit), 
				'description': str(self.description),
				'example': str(self.example), 
				'data_type': str(self.data_type), 
				'sort_order': int(self.sort_order)
				}
	
	
	
class Note(db.Model):
	
	group 		= db.StringProperty(indexed=True)
	heading		= db.StringProperty(indexed=True)
	sort_order 	= db.IntegerProperty(indexed=True)
	note 		= db.StringProperty()	
	
	def dic(self):
		return {'group': self.group,
				'note': self.note,
				'sort_order': self.sort_order
				}
				
				
				