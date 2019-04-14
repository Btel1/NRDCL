// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.query_reports["Daily Collection Report"] = {
	"filters": [
		{

                        "fieldname":"branch",
                        "label": ("Branch"),
                        "fieldtype": "Link",
                        "options": "Branch",
                        "width": "100",

                },
                {
                        "fieldname" : "from_date",
                        "label" : ("From Date"),
                        "fieldtype" : "Date",
			"default": frappe.defaults.get_user_default("year_start_date"),
			"width": "80"
                },
                {
                        "fieldname" : "to_date",
                        "label" : ("To Date"),
                        "fieldtype" : "Date",
			"default": get_today()
                },
		{
			"fieldname": "mode_of_paymnet",
			"label": __("Payment Mode"),
			"fieldtype": "Select",
			"options": ["", "Cheque Payment", "Cash paymnet"],
			"default": "",
			},
		{

                        "fieldname":"user",
                        "label": ("User"),
                        "fieldtype": "Link",
                        "options": "User",
                        "width": "100",

                },	

	]
}
