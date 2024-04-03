frappe.ready(function() {
    frappe.web_form.after_load = () => {
        frappe.web_form.on('dob', (field, value) => {
            if (value) {
                var dob = new Date(value);
                var today = new Date();
                var age = Math.floor((today - dob) / (365.25 * 24 * 60 * 60 * 1000));
                frappe.web_form.set_value("age", age.toString());
            }
        });
    };
});

