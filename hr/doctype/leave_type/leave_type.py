# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

from frappe.model.document import Document

class LeaveType(Document):
	def validate(self):
		if self.check_employment_status:
			if not self.employment_status:
				frappe.throw("Please select employment Status as you have check on <b>Maintain in Employee Master</b>")
	
