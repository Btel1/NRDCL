# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt
from frappe.utils.data import get_first_day, get_last_day

def execute(filters=None):
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data

def get_data(filters):
	doc_type = frappe.db.sql(""" select name from `tabData Entry List` where docstatus =1""", as_dict = 1)
	date = "creation between '{0}' and '{1}'".format(filters.get("from_date"), filters.get("to_date"))
        branch_name = ("'"+filters.get("branch")+"'") if filters.get("branch") else "branch"
	data1 = []
	data = []
	if not filters.get("transaction"):
		for doc in doc_type:
			doc1 = "tab"+"{0}".format(doc.name)
			#doc1 = "tab"+"{0}".format(doc.name)
			query = """
				select '{0}' as doctype, branch,
						sum(case when docstatus = 0 then 1 else 0 end) draft,
						sum(case when docstatus = 1 then 1 else 0 end) submitted,
						sum(case when docstatus = 2 then 1 else 0 end) cancelled,
						sum(case when docstatus in (0,1) then 1 else 0 end) total
					from `{1}` where branch = {2} and {3}
					group by doctype, branch
			""".format(doc.name, doc1, branch_name, date)
			data1 = frappe.db.sql(query, debug =1)
			data.extend(data1)
	else:
		doc2 = "tab"+"{0}".format(filters.get("transaction"))
		doc_na = "{0}".format(filters.get("transaction"))
		query = """
			select '{0}' as doctype, branch,
					sum(case when docstatus = 0 then 1 else 0 end) draft,
					sum(case when docstatus = 1 then 1 else 0 end) submitted,
					sum(case when docstatus = 2 then 1 else 0 end) cancelled,
					sum(case when docstatus in (0,1) then 1 else 0 end) total
				from `{1}` where branch = {2} and {3}
				group by doctype, branch
			""".format(doc_na, doc2, branch_name, date)
		data1 = frappe.db.sql(query, debug =1)
		data.extend(data1)
	return data

def get_columns(filters):
	cols = [
                ("Transaction") + ":Data:220",
		("Branch") + ":Data:220",
		("Draf(A)") + ":Int:110",
		("Submitted(B)") + ":Int:110",
		("Cancelled") + ":Int:110",
		("Total(A+B)") + ":Int:110",
	]
	return cols



