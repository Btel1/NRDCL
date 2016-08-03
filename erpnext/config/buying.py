from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Purchasing"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Material Request",
					"description": _("Request for purchase."),
				},
				{
					"type": "doctype",
					"name": "Request for Quotation",
					"description": _("Request for quotation."),
				},
				{
					"type": "doctype",
					"name": "Supplier Quotation",
					"label": "Vendor Quotation",
					"description": _("Quotations received from Suppliers."),
				},
				{
					"type": "doctype",
					"name": "Purchase Order",
					"description": _("Purchase Orders given to Suppliers."),
				},
			]
		},
		{
			"label": _("Vendors"),
			"items": [
				{
					"type": "doctype",
					"name": "Supplier",
					"label": "Vendor",
					"description": _("Supplier database."),
				},
				{
					"type": "doctype",
					"name": "Supplier Type",
					"label": "Vendor Type",
					"description": _("Supplier Type master.")
				},
				{
					"type": "doctype",
					"name": "Contact",
					"description": _("All Contacts."),
				},
				{
					"type": "doctype",
					"name": "Address",
					"description": _("All Addresses."),
				},

			]
		},
		{
			"label": _("Setup"),
			"icon": "icon-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Buying Settings",
					"description": _("Default settings for buying transactions.")
				},
				{
					"type": "doctype",
					"name":"Terms and Conditions",
					"label": _("Terms and Conditions Template"),
					"description": _("Template of terms or contract.")
				},
				{
					"type": "doctype",
					"name": "Purchase Taxes and Charges Template",
					"description": _("Tax template for buying transactions.")
				},
			]
		},
		{
			"label": _("Materials and Pricing"),
			"items": [
				{
					"type": "doctype",
					"name": "Item",
					"label": "Materials",
					"description": _("All Products or Services."),
				},
			#	{
			#		"type": "doctype",
			#		"name": "Product Bundle",
			#		"description": _("Bundle items at time of sale."),
			#	},
			#	{
			#		"type": "doctype",
			#		"name": "Price List",
			#		"description": _("Price List master.")
			#	},
				{
					"type": "doctype",
					"name": "Item Group",
					"icon": "icon-sitemap",
					"label": _("Material Group"),
					"link": "Tree/Item Group",
					"description": _("Tree of Item Groups."),
				},
				{
					"type": "doctype",
					"name": "Item Price",
					"label": "Material Price",
					"description": _("Multiple Item prices."),
					"route": "Report/Item Price"
				},
			#	{
			#		"type": "doctype",
			#		"name": "Pricing Rule",
			#		"description": _("Rules for applying pricing and discount.")
			#	},

			]
		},
		{
			"label": _("Analytics"),
			"icon": "icon-table",
			"items": [
				{
					"type": "page",
					"name": "purchase-analytics",
					"label": _("Purchase Analytics"),
					"icon": "icon-bar-chart",
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Supplier-Wise Sales Analytics",
					"doctype": "Stock Ledger Entry"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Purchase Order Trends",
					"doctype": "Purchase Order"
				},
			]
		},
		{
			"label": _("Other Reports"),
			"icon": "icon-list",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Materials To Be Requested",
					"doctype": "Item"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "PR Pending for PO",
					"doctype": "Material Request"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Supplier Quoation pending for PR",
					"doctype": "Material Request"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Material Purchase History",
					"doctype": "Item"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Vendor Addresses",
					"doctype": "Supplier"
				},
			]
		},
		{
			"label": _("Help"),
			"items": [
				{
					"type": "help",
					"label": _("Customer and Supplier"),
					"youtube_id": "anoGi_RpQ20"
				},
				{
					"type": "help",
					"label": _("Material Request to Purchase Order"),
					"youtube_id": "4TN9kPyfIqM"
				},
				{
					"type": "help",
					"label": _("Purchase Order to Payment"),
					"youtube_id": "EK65tLdVUDk"
				},
				{
					"type": "help",
					"label": _("Managing Subcontracting"),
					"youtube_id": "ThiMCC2DtKo"
				},
			]
		},
	]
