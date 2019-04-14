// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Timber Class', {
	refresh: function(frm) {
<<<<<<< HEAD
                disable_drag_drop(frm)
        },

        onload: function(frm) {
                disable_drag_drop(frm)
        },
});

function disable_drag_drop(frm) {
        frm.page.body.find('[data-fieldname="items"] [data-idx] .data-row').removeClass('sortable-handle');
}

frappe.ui.form.on('Royal Rate', {
        before_items_remove: function(frm, cdt, cdn) {
                doc = locals[cdt][cdn]
                if(!doc.__islocal) {
                        frappe.throw("Cannot delete saved Items")
                }
        }
})




=======

	}
});
>>>>>>> 8e631e56e9732fe4f351a3e1203675c0b67d9dc1
