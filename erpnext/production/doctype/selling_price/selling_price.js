// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Selling Price', {
	setup: function(frm) {
		frm.get_field('item_rates').grid.editable_fields = [
			{fieldname: 'price_based_on', columns: 3},
			{fieldname: 'particular', columns: 3},
			{fieldname: 'selling_price', columns: 3},
			{fieldname: 'item_sub_group', columns:3},
		]
	},

	refresh: function(frm) {

	}
});

frappe.ui.form.on('Selling Pricei Rate', {
       'price_based_on': function(frm, cdt, cdn) {
	val = locals[cdt][cdn]
	if(val.price_based_on === 'Item') {
	frm.add_fetch('particular', "item_name", "item_name")
	frm.refresh_field("item_name");
	frm.refresh_fields();
        }}
});

