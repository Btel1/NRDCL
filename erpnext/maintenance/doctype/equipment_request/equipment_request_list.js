frappe.listview_settings['Equipment Request'] = {
        add_fields: ["docstatus"],
        get_indicator: function(doc) {
                if(doc.docstatus == 1 && doc.ehf == null) {
                        return ["Requested", "orange", "docstatus,=,1"];
                }
                if(doc.docstatus == 1 && doc.ehf != null){
                        return ["Completed", "green", "docstatus ,=,1"];
                }
        }
};
