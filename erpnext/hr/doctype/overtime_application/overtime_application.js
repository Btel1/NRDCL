// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

cur_frm.add_fetch("employee", "employee_name", "employee_name")
cur_frm.add_fetch("employee", "branch", "branch")

frappe.ui.form.on('Overtime Application', {
	onload: function(frm) {
		if(!frm.doc.posting_date) {
			frm.set_value("posting_date", get_today())
		}
	},
	approver: function(frm) {
		if(frm.doc.approver){
			frm.set_value("approver_name", frappe.user.full_name(frm.doc.approver));
		}
	},
	employee: function(frm) {
		if (frm.doc.employee) {
			frappe.call({
				method: "erpnext.hr.doctype.employee.employee.get_overtime_rate",
				args: {
					employee: frm.doc.employee,
				},
				callback: function(r) {
					if(r.message) {
						frm.set_value("rate", r.message)
					}
				}
			})
		}	
	},
	rate: function(frm) {
		frm.set_value("total_amount", frm.doc.rate * frm.doc.total_hours)
	}
});


//Overtime Item  Details
frappe.ui.form.on("Overtime Application Item", {
	"number_of_hours": function(frm, cdt, cdn) {
		calculate_time(frm, cdt, cdn)
	},
})

function calculate_time(frm, cdt, cdn) {
	var total_time = 0;
	frm.doc.items.forEach(function(d) {
		if(d.number_of_hours) {
			total_time += d.number_of_hours
		}	
	})
	frm.set_value("total_hours", total_time)
	frm.set_value("total_amount", total_time * frm.doc.rate)
	cur_frm.refresh_field("total_hours")
	cur_frm.refresh_field("total_amount")
}
