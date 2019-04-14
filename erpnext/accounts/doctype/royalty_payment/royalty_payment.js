// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

cur_frm.add_fetch("branch", "cost_center", "cost_center")

frappe.ui.form.on('Royalty Payment', {
	onload: function(frm) {
                if (!frm.doc.posting_date) {
                        frm.set_value("posting_date", get_today());
                }
	},
	setup: function(frm) {
                frm.get_field('planned_items').grid.editable_fields = [
                        {fieldname: 'timber_class', columns: 2},
                        {fieldname: 'timber_type', columns: 2},
                        {fieldname: 'qty_cft', columns: 2},
                        {fieldname: 'log_rate', columns:2},
			{fieldname: 'log_percent', columns:2},
			{fieldname: 'log_amount', columns:2} 
                ]
        },

	refresh: function(frm) {

	},
	
	get_royalty_details: function(frm) {
		return frappe.call({
			method: "get_royalty_details",
			doc: frm.doc,
			callback: function(r, rt) {
				frm.refresh_field("planned_items");
				frm.refresh_field("adhoc_temp_items");
				frm.refresh_field("adhoc_items");
				frm.refresh_fields();
			},
			freeze: true,
			freeze_message: "Loading Royalty Details..... Please Wait"
		});
	}
});

frappe.ui.form.on("Royalty Payment", "refresh", function(frm) {
    cur_frm.set_query("marking_list", function() {
        return {
            "filters": {
                "branch": frm.doc.branch,
                "fmu": frm.doc.location,
		"docstatus": 1
            }
        };
    });

    cur_frm.set_query("location", function() {
        return {
            "filters": {
                "branch": frm.doc.branch,
		"is_disabled": 0
            }
        };
    });

    cur_frm.set_query("adhoc_production", function() {
        return {
            "filters": {
                "branch": frm.doc.branch,
                "location": frm.doc.location,
		"is_disabled": 0
            }
        };
    });
})
