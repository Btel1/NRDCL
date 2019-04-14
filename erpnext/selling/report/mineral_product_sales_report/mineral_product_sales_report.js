// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.query_reports["Mineral Product Sales Report"] = {
	"filters": [
		{
                        "fieldname": "from_date",
                        "label": __("From Date"),
                        "fieldtype": "Date",
                        "default": frappe.defaults.get_user_default("year_start_date"),
                },
                {
                        "fieldname": "to_date",
                        "label": __("To Date"),
                        "fieldtype": "Date",
                        "default": frappe.defaults.get_user_default("year_end_date"),
                },
		{
                        "fieldname": "sub_group",
                        "label": __("Item Sub Group"),
                        "fieldtype": "Select",
			//"defualt": run query report to get sub_group when item_group is Mineral Products
                        "options": ["Query Sand", "Drenched Sand", "RB Sand"]
                },
                {
                        "fieldname": "customer",
                        "label": __("Customer"),
                        "fieldtype": "Link",
                        "options": "Customer",
                }

	]
}
