function DebtorsDialog( confOb ){

var self = this;
this.initialising = true;


this.frm = new Ext.form.FormPanel({
	title: 'Foo',
	frame: true,
	bodyStyle: 'padding: 20px;',
	labelAlign: 'right',
	
	items:[
		{xtype: 'textfield', fieldLabel: 'Contact', name: 'contact'},
		{xtype: 'textfield', fieldLabel: 'Company', name: 'company'},
		{xtype: 'textarea',  fieldLabel: 'Address', name: 'address'},
		{xtype: 'textfield', fieldLabel: 'Postcode', name: 'postcode'},
		{xtype: 'textfield', fieldLabel: 'Telephone', name: 'tel'},
		{xtype: 'textfield', fieldLabel: 'Fax', name: 'fax'},
	]

});

this.win = new Ext.Window({
	title: confOb.id == 0 ? 'New Debtor': 'Edit Debtor',
	width: 500,
	items: [ this.frm ],
	buttons: [
		{text: 'Cancel', iconCls: 'icoBlack', 
			handler: function(){
				self.win.close();
			}
		},
		{text: 'Save', iconCls: 'icoSave',
			handler: function(){

			}
		}
	]
});

this.win.show();

}
