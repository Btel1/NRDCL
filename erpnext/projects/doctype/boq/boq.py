# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt
'''
--------------------------------------------------------------------------------------------------------------------------
Version          Author          CreatedOn          ModifiedOn          Remarks
------------ --------------- ------------------ -------------------  -----------------------------------------------------
1.0		  SHIV		                    2017/08/15         Original Version
--------------------------------------------------------------------------------------------------------------------------                                                                          
'''
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.model.naming import make_autoname
from frappe.utils import cstr, flt

class BOQ(Document):
        """
        def autoname(self):
                self.name = make_autoname(str('BOQ')+'.YYYY.MM.####')
        """
                
	def validate(self):
                self.update_defaults()
                self.validate_defaults()

        def on_submit(self):
                self.update_project_value()

        def on_cancel(self):
                self.update_project_value()
                
        def validate_defaults(self):
                if not self.project:
                        frappe.throw("`Project` cannot be null.")
                        
                if not self.branch:
                        frappe.throw("`Branch` cannot be null.")

                if not self.cost_center:
                        frappe.throw("`Cost Center` cannot be null.")
                        
        def update_defaults(self):
                item_group = ""
                self.claimed_amount = 0
                self.received_amount = 0
                self.balance_amount = 0
                
                for item in self.boq_item:
                        if item.is_group:
                                item_group = item.item

                        item.parent_item = item_group
                        self.claimed_amount  += flt(item.claimed_amount)
                        self.received_amount += flt(item.received_amount)
                        self.balance_amount += (flt(item.amount)-flt(item.received_amount))

                # Defaults
                if not self.branch:
                        self.branch = frappe.db.get_value("Project", self.project, "branch")

                if not self.cost_center:
                        self.cost_center = frappe.db.get_value("Project", self.project, "cost_center")

        def update_project_value(self):
                boq = frappe.db.sql("""
                                        select sum(ifnull(total_amount,0)) total_amount
                                        from `tabBOQ`
                                        where project = '{0}'
                                        and   docstatus = 1
                                """.format(self.project), as_dict=1)[0]

                if flt(boq.total_amount) > 0:
                        frappe.db.sql("""
                                update `tabProject`
                                set project_value = {0}
                                where name = '{1}'
                        """.format(flt(boq.total_amount), self.project))
        
@frappe.whitelist()
def make_project_invoice(source_name, target_doc=None):
        def update_master(source_doc, target_doc, source_parent):
                target_doc.invoice_title = str(target_doc.project) + "(Project Invoice)"
                target_doc.check_all = 1
                
        def update_item(source_doc, target_doc, source_parent):
                target_doc.act_quantity = flt(target_doc.invoice_quantity)
                target_doc.act_rate     = flt(target_doc.invoice_rate)
                target_doc.act_amount   = flt(target_doc.invoice_amount)
                target_doc.original_rate= flt(target_doc.invoice_rate)
                
        doclist = get_mapped_doc("BOQ", source_name, {
                "BOQ": {
                        "doctype": "Project Invoice",
                        "field_map": {
                                "project": "project"
                        },
                        "postprocess": update_master
                },

                "BOQ Item": {
                        "doctype": "Project Invoice BOQ",
                        "field_map": {
                                "name": "boq_item_name",
                                "balance_quantity": "invoice_quantity",
                                "rate": "invoice_rate",
                                "balance_amount": "invoice_amount",
                                "quantity": "original_quantity",
                                "amount": "original_amount"
                        },
                        "postprocess": update_item
                }
        }, target_doc)

        return doclist

@frappe.whitelist()
def make_book_entry(source_name, target_doc=None):
        def update_master(source_doc, target_doc, source_parent):
                target_doc.check_all = 1
                
        def update_item(source_doc, target_doc, source_parent):
                target_doc.act_quantity = flt(target_doc.entry_quantity)
                target_doc.act_rate     = flt(target_doc.entry_rate)
                target_doc.act_amount   = flt(target_doc.entry_amount)
                target_doc.original_rate= flt(target_doc.entry_rate)
                
        doclist = get_mapped_doc("BOQ", source_name, {
                "BOQ": {
                        "doctype": "MB Entry",
                        "field_map": {
                                "project": "project"
                        },
                        "postprocess": update_master
                },

                "BOQ Item": {
                        "doctype": "MB Entry BOQ",
                        "field_map": {
                                "name": "boq_item_name",
                                "balance_quantity": "entry_quantity",
                                "rate": "entry_rate",
                                "balance_amount": "entry_amount",
                                "quantity": "original_quantity",
                                "amount": "original_amount"
                        },
                        "postprocess": update_item
                }
        }, target_doc)

        return doclist
