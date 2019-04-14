# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
def execute(filters=None):
	columns = get_columns()
	frappe.msgprint("{0}".format(len(columns)))
	data = 'tashi'
	#for i in xrange(19:
	#data.append(i)		
	return columns, data

def get_columns():
	return [
		{"fieldname": "item_code", "label": _("Item Code"), "fieldtype": "Link", "options":"Item", "width": 150},
		{"fieldname": "item_name", "label": _("Item Name"), "fieldtype": "Data",  "width": 150},
		{"fieldname": "customer_id", "label": _("Customer ID"), "fieldtype": "Link", "options":"Customer", "width": 150},
		{"fieldname": "customer_name", "label": _("Customer Name"), "fieldtype": "Data", "width": 150},
		{"fieldname": "customer_type", "label": _("Customer Type"), "fieldtype": "Data",  "width": 150},
		{"fieldname": "customer_cid", "label": _("Customer CID/Work Permit"), "fieldtype": "Data",  "width": 150},
		{"fieldname": "contact_no", "label": _("Contact No"), "fieldtype": "Data", "width": 150},
		{"fieldname": "plot_thram_no", "label": _("Plot/Thram No"), "fieldtype": "Data", "width": 150},
		{"fieldname": "location", "label": _("Destination"), "fieldtype": "Data", "width": 150},
		{"fieldname": "vehicle_no", "label": _("Vehicle No"), "fieldtype": "Data", "width": 150},
		{"fieldname": "vehicle_capacity", "label": _("Vehicle Capacity"), "fieldtype": "Data", "width": 150},
		{"fieldname": "driver_name", "label": _("Driver's Name"), "fieldtype": "Data", "width": 150},
		{"fieldname": "driver_contact_no", "label": _("Driver Contact No"), "fieldtype": "Data", "width": 150},
		{"fieldname": "current__address", "label": _("Current Address"), "fieldtype": "Data", "width": 150},
		{"fieldname": "qty_required", "label": _("Quantity Required(UOM)"), "fieldtype": "Data", "width": 150},
		{"fieldname": "qty_approved", "label": _("Quantity Appoved(UOM)"), "fieldtype": "Data", "width": 150},
		{"fieldname": "balance_qty", "label": _("Balanced Qty.(UOM)"), "fieldtype": "Data", "width": 150},
		{"fieldname": "rate", "label": _("Rate"), "fieldtype": "Data", "width": 150},
		{"fieldname": "amount", "label": _("Amount"), "fieldtype": "Data", "width": 150},

	]


