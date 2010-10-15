# -*- coding: utf-8 -*-

from tipfy import RequestHandler, Response, render_json_response
from tipfy.ext.jinja2 import render_response


from apps.app_global import AppGlobal
appGlobal = AppGlobal()


##########################################################################
class IndexHandler(RequestHandler):
	def get(self):
		"""Simply returns a rendered template with an enigmatic salutation."""#
		context = {'title': 'Index', 'tab': '/'}
		return render_response('index.html', c=context, g=appGlobal)


##########################################################################
class DebtorsHandler(RequestHandler):
	def get(self):
		context = {'title': 'Debtors', 'tab': '/debtors'}
		return render_response('debtors.html', c=context, g=appGlobal)


##########################################################################
class AccountsHandler(RequestHandler):
	def get(self):
		context = {'title': 'Accounts', 'tab': '/accounts'}
		return render_response('accounts.html', c=context, g=appGlobal)













##########################################################################
class CssIconsHandler(RequestHandler):
	
	def get(self, group=None):
		
		#payload = {'success': True}

		#ggroups = queries.groups()
	
		#return render_response('ags4.html' , groups=ggroups, g=appGlobal, c={})
		

		
		icons = {}

		icons['icoAgsClasses'] = 'shape_align_left.png'
		icons['icoAgsGroups'] = 'shape_move_back.png'
		icons['icoAgsHeadings'] = 'shape_ungroup.png'
		#icons['icoAgsClasses'] = ''


		icons['icoInvis'] = 'transparent.png';

		icons['icoDashBoard'] = 'plugin.png';
		icons['icoLanServer'] = 'server.png';
		
		##/* Widgets **************************************/
		icons['icoAdd'] = 'add.png';
		icons['icoEdit'] = 'page_white_edit.png';
		icons['icoDelete'] = 'delete.png';
		icons['icoMerge'] = 'shape_ungroup.png';

		icons['icoHelp'] = 'help.png';
		icons['icoHome'] = 'house.png';

		icons['icoRefresh'] = 'arrow_refresh.png';
		icons['icoRefresh2'] = 'refresh.gif';
		#icons['icoGo'] = 'arrow_rotate_clockwise.png';
		icons['icoSave'] = 'accept.png';
		icons['icoCancel'] = 'bullet_black.png';
		icons['icoClipboard'] = 'page_paste.png';
		icons['icoGo'] = 'bullet_go.png';
		icons['icoClose'] = 'cross.png';

		#icons['icoMore'] = 'bullet_arrow_down.png';
		icons['icoShowMore'] = 'zoom_in.png';
		icons['icoShowLess'] = 'zoom_out.png';



		icons['icoEmail'] = 'email.png';
		icons['icoSms'] = 'phone.png';
		icons['icoTel'] = 'telephone.png';
		icons['icoFax'] = 'newspaper.png';
		icons['icoMessage'] = 'text_signature.png';
		icons['icoFreeText'] = 'textfield.png';


		##/* Widgets **************************************/
		icons['icoBlack'] = 'bullet_black.png';
		icons['icoBlue'] = 'bullet_blue.png';
		icons['icoGreen'] = 'bullet_green.png';
		icons['icoOrange'] = 'bullet_orange.png';
		icons['icoPink'] = 'bullet_pink.png';
		icons['icoPurlple'] = 'bullet_purple.png';
		icons['icoRed'] = 'bullet_red.png';
		icons['icoYellow'] = 'bullet_yellow.png';
		icons['icoDetails'] =  'bullet_white.png';

		icons['icoSearch'] = 'find.png';


		##/* Form **************************************/
		icons['icoClean'] = 'bullet_black.png';
		icons['icoDirty'] = 'bullet_red.png';


		##/* Wizzard **************************************/
		icons['icoNext'] = 'arrow_right.png';
		icons['icoPrev'] = 'arrow_left.png';
		icons['icoWizard'] = 'wand.png';

		icons['icoForward'] = 'arrow_right.png';
		icons['icoBack'] = 'arrow_left.png';

		icons['icoBrowse'] = 'browse.png';

		###/* Actions **************************************/
		#//icons['icoUpload'] = 'arrow_up.png';
		#//icons['icoDownload'] = 'arrow_down.png';
		icons['icoUpload'] = 'page_white_get.png';
		icons['icoDownload'] = 'page_white_put.png';

		icons['icoQuit'] = 'control_eject.png';
		icons['icoLogin'] = 'connect.png';


	

		icons['icoContact'] = 'user.png';
		icons['icoContactView'] = 'user.png';
		icons['icoContactAdd'] = 'user_add.png';
		icons['icoContactDelete'] = 'user_delete.png';
		icons['icoContactEdit'] = 'user_edit.png';



		icons['icoFile'] = 'geo_job.png';
		icons['icoFileOpen'] = 'page_white_go.png';
		icons['icoFileCopy'] = 'page_white_copy.png';
		icons['icoFileRename'] = 'page_white_edit.png';
		icons['icoFileDelete'] = 'page_white_delete.png';





		#/* Samples */
		#/* icons['icoSamples'] = 'package_green.png';
		icons['icoSample'] = 'package.png';
		icons['icoSampleAdd'] = 'package_add.png';
		icons['icoSampleDelete'] = 'package_delete.png';
		#*/
		icons['icoSamples'] = 'tag_blue.png';
		icons['icoSample'] = 'tag_green.png';
		icons['icoSampleAdd'] = 'tag_blue_add.png';
		icons['icoSampleDelete'] = 'tag_blue_delete.png';


		##/* Test */
		icons['icoTest'] = 'chart_line.png';
		icons['icoTestAdd'] = 'chart_line_add.png';
		icons['icoTestEdit'] = 'chart_line_edit.png';
		icons['icoTestDelete'] = 'chart_line_delete.png';
		icons['icoReport'] = 'chart_curve.png';




		icons['icoWeekView'] = 'calendar_view_week.png';


		icons['icoOn'] = 'bullet_green.png';
		icons['icoOff'] = 'bullet_black.png';

		icons['icoFilterOn'] = 'bullet_pink.png';
		icons['icoFilterOff'] = 'bullet_purple.png';

		icons['icoStart'] = 'control_play_blue.png';
		icons['icoEnd'] = 'control_stop_blue.png';

		icons['icoError'] = 'exclamation.png';

		icons['icoDiggs'] = 'database_table.png';
		icons['icoSettings'] = 'plugin.png';







		icons['icoShortcuts'] = 'arrow_inout.png';
		icons['icoDev'] = 'wand.png';

		icons['icoMerge'] = 'table_relationship.png';

		icons['icoFolder'] = 'folder.png';
		icons['icoFolderAdd'] = 'folder_add.png';



		icons['icoRootTree'] = 'sitemap_color.png';
		icons['icoUsers'] = 'group_gear.png';

		

		#//** Just include this file OK
		#if(!defined('STOP_ME_SPOOLING_ICON')){

		#$IconServerPath =   file_exists('../LOCAL') 
		#					? 'http://localhost/~test/famfamfam_silk_icons_v013/icons/'
		#					: 'http://ico.daffodil.uk.com/'
		#	
		#	foreach($desktop_icons as $k => $v){
		IconServerPath = 'http://ico.daffodil.uk.com'
		s = ''
		for k in sorted(icons.keys()):
			#s += "%s = %s\n" % (k, icons[k])
			s += ".%s{background-image: url('%s/%s') !important;}\n" % (k, IconServerPath, icons[k])

		s += "\n\n" # incase
		#response.headers['Content-Type'] = 'image/png'
		#response.headers['content-type'] = 'text/css'
		response = Response(s)
		response.headers['Content-Type'] = 'text/css'
		# Return a rendered template
		#return render('/style.mako')
		# or, return a response
		return response