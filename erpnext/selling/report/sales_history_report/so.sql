query = "select t1.name as sales_no, t1.transaction_date as sales_date, t1.customer, 
	t1.po_no, t1.po_date, t1.base_net_amount, t1.rate, t1.qty, t1.item_name, t1.item_code,
     t1.stock_uom, t1.warehouse, t1.delivery_note, t1.delivery_date,
     t2.invoice_no, t2.ref_date, t2.posting_date, t2.due_date, t2.write_off_amount, t2.write_off_description, 
     t2.total_advance, t1.transporter_name, t2.delivered_qty, t2.accepted_qty, 
     t2.amount, t2.normal_loss_amt, t2.remarks, t2.abnormal_loss_amt, t2.justification, t2.excess_amt, 
     t2.excess_qty 
     from (select so.name, so.transaction_date, so.customer, so.po_no, so.po_date, soi.base_net_amount, 
     soi.rate, soi.qty, soi.item_name, soi.item_code, soi.stock_uom, soi.warehouse, dni.parent as delivery_note,
      (select transporter_name1 from `tabDelivery Note` as dn where dn.name = dni.parent) as transporter_name, 
      (select posting_date from `tabDelivery Note` as dn where dn.name = dni.parent) as delivery_date from 
      (`tabSales Order` as so JOIN `tabSales Order Item` as soi on so.name = soi.parent and so.docstatus = 1) 
      LEFT JOIN `tabDelivery Note Item` as dni on so.name = dni.against_sales_order and dni.docstatus = 1) as t1 
      left join (select si.name as invoice_no, si.sales_invoice_date as ref_date, si.posting_date, 
      si.due_date, si.write_off_amount, si.write_off_description, si.total_advance, sii.accepted_qty, 
      sii.delivered_qty, sii.amount, sii.normal_loss_amt, sii.remarks, 
      sii.abnormal_loss_amt, sii.justification, sii.excess_amt, sii.excess_qty, 
      sii.delivery_note as delivery_note_no from `tabSales Invoice` as si, `tabSales Invoice Item` as sii 
      where si.name = sii.parent and si.docstatus = 1) as t2 on t1.delivery_note = t2.delivery_note_no"

select t1.name as sales_no, t1.customer, 
	t1.po_no, t1.transaction_date, t1.rate, t1.qty, t1.item_name, t1.item_code,
     t1.stock_uom, t1.warehouse, t1.delivery_note,
     t2.invoice_no, t2.posting_date 
     from (select so.name, so.customer, so.po_no, so.transaction_date,
     soi.rate, soi.qty, soi.item_name, soi.item_code, soi.stock_uom, soi.warehouse, dni.parent as delivery_note, 
      (select dn.transportation_charges from `tabDelivery Note` as dn
      where dn.name = dni.parent) as delivery_date from 
      (`tabSales Order` as so JOIN `tabSales Order Item` as soi on so.name = soi.parent and so.docstatus = 1) 
      inner JOIN `tabDelivery Note Item` as dni on so.name = dni.against_sales_order and dni.docstatus = 1) as t1
      inner join (select si.name as invoice_no, si.posting_date, sii.delivery_note as delivery_note_no 
      from `tabSales Invoice` as si, `tabSales Invoice Item` as sii 
      where si.name = sii.parent and si.docstatus = 1) as t2 on t1.delivery_note = t2.delivery_note_no