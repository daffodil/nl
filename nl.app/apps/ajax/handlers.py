# -*- coding: utf-8 -*-
"""
	handlers
	~~~~~~~~

	:copyright: 2009 by tipfy.org.
	:license: BSD, see LICENSE for more details.
"""

import datetime
from tipfy import RequestHandler, Response, render_json_response
from tipfy.ext.jinja2 import render_response

from google.appengine.ext import db
from google.appengine.api import memcache

from apps.app_global import AppGlobal
from apps import queries

from tipfy.ext.db import get_or_insert_with_flag

#from django.utils import simplejson as json

from apps.models import Group, Heading, Note, Abbrev, AbbrevCode, AgsFile

appGlobal = AppGlobal()

class Context:
	pass


##########################################################################
class AbbrevsAjaxHandler(RequestHandler):
	
	def get(self):
		payload = {'success': True}
		
		#class_filter =  self.request.args.get('class')
		
		payload['abbrevs'] = queries.abbrevs()
		return render_json_response(payload)


##########################################################################
class AbbrevAjaxHandler(RequestHandler):
	
	def get(self, abbrev_requested):
		payload = {'success': True}
		
		A = Abbrev.get_by_key_name(abbrev_requested)
		if A:
			#payload = {'abbrev': {}}
			payload['table'] = A.dic()
			query = db.GqlQuery("select * from AbbrevCode where table=:1", A.table)
			results = query.fetch(2000)
			payload['abbrev_codes'] = [r.dic() for r in results]
		else:
			payload['error'] = "Abbrev table '%s' not found" % abbrev_requested
			
		return render_json_response(payload)	
	
	def post(self, abbrev_requested):
		
		## Check if this is a json_import port
		ptable = self.request.form.get('table')
		#cls = self.request.form.get('class')
		description = self.request.form.get('description')
		
		if ptable and ptable == abbrev_requested:
			#g = json.loads(group_str)
			payload = {'success': True}
			#q = db.GqlQuery("select * from group where group=:1", g['group'])
			#G = g.get()
			A = Abbrev.get_by_key_name(ptable)
			if A == None:
				A = Abbrev(key_name=ptable, table=ptable, description=description)
				A.put()
				payload['action'] = 'new'
				
			else:
				#G.cls = cls
				A.description = description
				payload['action'] = 'updated'
				A.put()
			payload['group'] = A.dic()
		else:
			payload = {'error': 'url/group mismatches'}
		#return render_response('container.html', c=context, g=appGlobal)
		return render_json_response(payload)


##########################################################################
class AbbrevCodeAjaxHandler(RequestHandler):
	#def get(self, abbrev_requested, code_requested):
		#return self.post(abbrev_requested, code_requested)
	
	def post(self, abbrev_requested):
		
		## Check if this is a json_import port
		ptable = self.request.form.get('table')
		pcode = self.request.form.get('code')
		
		description = self.request.form.get('description')
		date_added_str = self.request.form.get('date_added')
		added_by = self.request.form.get('added_by')
		
		#if date_added != "":
		date_parts = date_added_str.split("-")
		date_added = datetime.date(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))
		
		if ptable and ptable == abbrev_requested:
			#g = json.loads(group_str)
			payload = {'success': True}
			#q = db.GqlQuery("select * from group where group=:1", g['group'])
			#G = g.get()
			A = Abbrev.get_by_key_name(ptable)
			if A == None:
				#A = Abbrev(key_name=ptable, table=ptable, description=description)
				#A.put()
				payload['error'] = "AbbrevTable '%s' not found" % ptable
				
			else:
				query = db.GqlQuery("select * from AbbrevCode where table=:1 and code=:2", ptable, pcode)
				AC = query.get()
				if AC == None:
					AC = AbbrevCode(key_name="%s/%s" % (ptable, pcode), 
									table=ptable, code=pcode, 
									description=description,
									date_added=date_added, added_by=added_by
									)
					payload['action'] = 'added'
				else:
					#if AC.description != description:
					AC.description = description
					#AC.date_added = date_added
					modi = True
					#if 
					payload['action'] = 'updated'
				AC.put()
			payload['abbrev_code'] = AC.dic()
		else:
			payload = {'error': 'url/group mismatches'}
		#return render_response('container.html', c=context, g=appGlobal)
		return render_json_response(payload)


##########################################################################
class DEADGroupsAjaxHandler(RequestHandler):
	
	def get(self):
		payload = {'success': True}
		
		class_filter =  self.request.args.get('class')
		if class_filter == 'All':
			class_filter = None
		search_text =  self.request.args.get('search_text')
		search_col =  self.request.args.get('search_col')
		
		payload['groups'] = queries.groups(class_filter=class_filter, search_text=search_text, search_col=search_col)
		return render_json_response(payload)

##########################################################################
class GroupsHandler(RequestHandler):
	
	def get(self, version, ext=None):
		payload = {'success': True, 'version': version, 'ext': ext}
		
		class_filter =  self.request.args.get('class')
		if class_filter == 'All':
			class_filter = None
		search_text =  self.request.args.get('search_text')
		search_col =  self.request.args.get('search_col')
		
		
		
		payload['groups'] = queries.groups(class_filter=class_filter, search_text=search_text, search_col=search_col)
		return render_json_response(payload)
		
##########################################################################
# ? debug not prod
class GroupsMetaAjaxHandler(RequestHandler):
	
	def get(self):
		payload = {'success': True}
		
		
		
		payload['groups_meta'] = queries.groups_meta()
		return render_json_response(payload)


##########################################################################
class GroupAjaxHandler(RequestHandler):
	
	def get(self, group_requested):
		
		payload = {'success': True}
		
		G = Group.get_by_key_name(group_requested)
		if G:
			query = db.GqlQuery("select * from Heading where group=:1 order by sort_order", G.name)
			heading_objects = query.fetch(1000)
			headings = []
			for h in heading_objects:
				headings.append(h.dic())
			payload['group'] = G.dic()
			payload['headings'] = headings
		else:
			payload['error'] = 'Group %s not found' % group_requested
		
		return render_json_response(payload)
	
	def post(self, group_requested):
		
		## Check if this is a json_import port
		pgroup = self.request.form.get('group')
		cls = self.request.form.get('class')
		description = self.request.form.get('description')
		if pgroup and pgroup == group_requested:
			#g = json.loads(group_str)
			payload = {'success': True}
			G = Group.get_by_key_name(pgroup)
			if G == None:
				G = Group(key_name=pgroup, name=pgroup, cls=cls, description=description)
				G.put()
				payload['action'] = 'new'
				
			else:
				G.cls = cls
				G.description = description
				payload['action'] = 'updated'
				G.put()
			payload['group'] = G.dic()
		else:
			payload = {'error': 'url/group mismatches'}
		#return render_response('container.html', c=context, g=appGlobal)
		return render_json_response(payload)



"""status": "*", "description": "Sample type", "data_type": "PA", "heading": "SAMP_TYPE", "rev_date": "", "example": "U", "unit": ""
"""
##########################################################################
class GroupHeadingsAjaxHandler(RequestHandler):
	
	def get(self, group_requested):
		
		payload = {'success': True}
		query = db.GqlQuery("select * from Heading where group=:1 order by sort_order ASC", group_requested)
		results = query.fetch(1000)
		payload['headings'] = [ r.dic() for r in results ]
		#if F:
			#payload['field'] = [F.dic()]
		#else:
			#payload['error'] = "Field '%s/%s/' Not Found" % (group_requested, heading_requested)
	
		return render_json_response(payload)
	
	
##########################################################################
class GroupNotesAjaxHandler(RequestHandler):
	
	def get(self, group_requested):
		
		payload = {'success': True}
		
		query = db.GqlQuery("select * from Note where group=:1 order by sort_order ASC", group_requested)
		results = query.fetch(1000)
		payload['notes'] = [ r.dic() for r in results ]
	
		return render_json_response(payload)
		
##########################################################################
class HeadingAjaxHandler(RequestHandler):
	
	def get(self, group_requested, heading_requested):
		
		payload = {'success': True}
		query = db.GqlQuery("select * from Heading where group=:1 and field=:2", 
							group_requested, heading_requested)
		F = query.get()
		if F:
			payload['field'] = [F.dic()]
		else:
			payload['error'] = "Heading '%s/%s/' Not Found" % (group_requested, heading_requested)
	
		return render_json_response(payload)
	
	def post(self, group_requested, heading_requested):
		

		pgroup = self.request.form.get('group')
		pfield = self.request.form.get('name') ##### TODO
	
		payload = {'success': True, 'V': [group_requested, pgroup, heading_requested, pfield]}
		"""
		{u'status': u'', u'description': u'Project title', u'data_type': u'X', u'heading': u'PROJ_NAME', u'unit': u'', u'example': u'ACME Gas Works Redevelopment', u'rev_date': u''}
		"""
		if pgroup and pfield and pgroup == group_requested and pfield == heading_requested:
			
			G = Group.get_by_key_name(pgroup)
			if G:
				status =  self.request.form.get('status')
				description =  self.request.form.get('description')
				data_type =  self.request.form.get('data_type')
				unit =  self.request.form.get('unit')
				example =  self.request.form.get('example')
				sort_order = int(self.request.form.get('sort_order'))
				
				query = db.GqlQuery("select * from Heading where group=:1 and name=:2", pgroup, pfield)
				H = query.get()
				if not H:
					H = Heading(key_name="%s/%s" % (pgroup, pfield), group=pgroup, name=pfield)
				
				H.unit = unit
				H.description = description
				H.status = status
				H.data_type = data_type
				H.example = example
				H.sort_order = sort_order
				H.put()
				payload['heading'] = H.dic()
			
			else:
				payload['error'] = 'group %s does not exist' % pgroup
		else:
			payload['error'] =  'Mismatched request vars'
		#return render_response('container.html', c=context, g=appGlobal)
		return render_json_response(payload)


##########################################################################
class NoteAjaxHandler(RequestHandler):
	
	def get(self, group_requested, note_requested):
		
		payload = {'success': True}
		query = db.GqlQuery("select * from Note where group=:1 and key_name=:2", 
							group_requested, note_requested)
		F = query.get()
		if F:
			payload['heading'] = [F.dic()]
		else:
			payload['error'] = "Field '%s/%s/' Not Found" % (group_requested, heading_requested)
	
		return render_json_response(payload)
	
	def post(self, group_requested, heading_requested):
		

		pgroup = self.request.form.get('group')
		pfield = self.request.form.get('name') ##### TODO
	
		payload = {'success': True, 'V': [group_requested, pgroup, heading_requested, pfield]}
		"""
		{u'status': u'', u'description': u'Project title', u'data_type': u'X', u'heading': u'PROJ_NAME', u'unit': u'', u'example': u'ACME Gas Works Redevelopment', u'rev_date': u''}
		"""
		if pgroup and pfield and pgroup == group_requested and pfield == heading_requested:
			
			G = Group.get_by_key_name(pgroup)
			if G:
				status =  self.request.form.get('status')
				description =  self.request.form.get('description')
				data_type =  self.request.form.get('data_type')
				unit =  self.request.form.get('unit')
				example =  self.request.form.get('example')
				sort_order = int(self.request.form.get('sort_order'))
				
				query = db.GqlQuery("select * from Heading where group=:1 and field=:2", pgroup, pfield)
				F = query.get()
				if not F:
					F = Field(key_name="%s/%s" % (pgroup, pfield), group=pgroup, field=pfield)
				
				F.unit = unit
				F.description = description
				F.status = status
				F.data_type = data_type
				F.example = example
				F.sort_order = sort_order
				F.put()
				#payload['field'] = F.dic()
			
			else:
				payload['error'] = 'group %s does not exist' % pgroup
		else:
			payload['error'] =  'Mismatched request vars'
		#return render_response('container.html', c=context, g=appGlobal)
		return render_json_response(payload)





##########################################################################
class ClassesAjaxHandler(RequestHandler):
	
	def get(self):
		payload = {'success': True}
		payload['classes'] = queries.classes()
		return render_json_response(payload)
	
	

##########################################################################
class MemcacheAjaxHandler(RequestHandler):
	def get(self):
		payload = {'success': True}
		payload['flush_all'] = memcache.flush_all()
		return render_json_response(payload)
		
			
##########################################################################
class ViewFileAjaxHandler(RequestHandler):
	def get(self):
		
		payload = {'success': True}
		query = AgsFile.all()
		F = query.get()
		
		#payload['ags_file'] = F.dic()
		
		from apps.ags import Ags4Parser
		P = Ags4Parser(F.contents)
		payload['ags_data'] = P.meta()
		#payload['ags_data'] = groups
		#payload['data'] = data
		
		return render_json_response(payload)

	
	

		

