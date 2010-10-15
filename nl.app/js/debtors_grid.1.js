

function DebtorsGrid( confOb ){

var self = this;
this.initialising = true;

//********************************************************************************
//** Classes
//********************************************************************************
this.store = new Ext.data.JsonStore({
	proxy: new Ext.data.HttpProxy({url: '/json/debtors', method: 'GET'}),
	root: 'debtors',
	idProperty: 'class',
	sortInfo: {field: 'class', direction: 'ASC'},
	fields: [
			 'contact', 'company', 'address','postcode','tel','fax','amount'
	]
});


this.selModel = new Ext.grid.RowSelectionModel({
	singleSelect: true, hidden: true
});




this.searchStore = new Ext.data.ArrayStore({
	
	fields: ['val','label'],
	data: [
		['all', 'All'], ['code', 'Code'], ['description', 'Description']
	]
});

//*******************************************************
//*** Search Form 
//*******************************************************
this.searchText = new Ext.form.TextField({
	fieldLabel: 'For',  width: 150, 
	allowBlank: false, minLength: 3,
	enableKeyEvents: true	
});
this.searchText.on("keyup", function(txt, e){
	//console.log(txt, e);
	var txt =  self.searchText.getValue();
	var auto = self.searchForm.getForm().findField('autosubmit').getValue();
	//console.log(auto, txt);
	if( auto ){
		if(txt.length > 2){
			self.storeGroups.load({params: {search_text: txt}});
			return;
		}
	}
	//TODO enter pressed
});

this.searchForm = new Ext.FormPanel({
	title: 'Search Groups',
	bodyStyle: 'padding: 20px',
	labelWidth: 100,
	frame: true,
	labelAlign: 'right',
	items: [
		{xtype: 'combo', fieldLabel: 'Search in', name: 'search_col', value: 'description',
			store: this.searchStore, width: 150, 
			triggerAction: 'all', mode: 'local',
			valueField: 'val', displayField: 'label'
		},
		this.searchText,
		{xtype: 'checkbox', 
			boxLabel: 'Autosubmit after three characters', 
			hideLabel: true, 
			checked: true, 
			name: 'autosubmit'
		}
		
	],
	buttons: [
		new Ext.Button({
			text: 'Submit', 
			iconCls: 'icoGo'	
		})
	]
		
});



this.actionAdd = new Ext.Action({
	text: 'New',
	iconCls: 'icoAdd',
});
this.actionEdit = new Ext.Action({
	text: 'Edit',
	iconCls: 'icoEdit',
});
this.actionDelete = new Ext.Action({
	text: 'Delete',
	iconCls: 'icoDelete',
});

this.statusBar = new Ext.ux.StatusBar({text: 'No debtores in this view'});


//************************************************************************************
this.grid = new Ext.grid.GridPanel({
	title: 'Debtors',
	hideTitle: true,
	renderTo: 'debtors_widget',
	iconCls: 'icoAgsGroups',
	border: false,
	height: window.innerHeight - 140,
	tbar: [this.actionAdd, this.actionEdit, this.actionDelete],
	colModel: new Ext.grid.ColumnModel({
		defaults: {
			CCCwidth: 120,
			sortable: true
			
		},
		columns:[
					{dataIndex: 'name', header: 'Group', width: 50},
					{dataIndex: 'description', header: 'Description'}
					//{dataIndex: 'class', header: 'Class'},
		]
	}),
	store: this.store,
	sm: this.selModel,
	loadMask: true,
	stripeRows: true,
	enableHdMenu: false,
	viewConfig: {forceFit: true,  deferEmptyText: false, emptyText: 'No debtors in this list'},
	bbar: [ this.statusBar ]
});



this.initialising = false;

this.load = function(){
	if(this.initialising === false){
			//var combo = self.searchForm.getForm().findField('search_col')
			//console.log("combo",combo)
			//combo.select(2);
	}
	self.storeClasses.load();
	
	self.storeGroups.load();
};

//self.load();
//self.storeAbbrevs.load();
	//self.storeClasses.load();
}

/* Ags2Go_Widget() */


