// Copyright (c) 2024, akshay and contributors
// For license information, please see license.txt

// frappe.ui.form.on("vehicle Detail", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('vehicle Detail', {
    refresh: function(frm) {
        frm.add_custom_button(__('Add Field'), function() {
            frappe.prompt([
                {'fieldname': 'fuel_type', 'fieldtype': 'Select', "options": "Petrol\nDiesel\nCNG\nElectric\nHybrid",'label': 'Select Fuel Type'},
                {'fieldname': 'transmission_type', 'fieldtype': 'Select',"options": "Automatic\nManual", 'label': 'Select Transmission Type'},
                {'fieldname': 'no_of_owners', 'fieldtype': 'Select', "options": "1st\n2nd\n3rd\n4th\n4+", 'label': 'Enter No Of Owners'},
            ],
            function(values){
                console.log(values.fuel_type,"values")
                var child1 = frm.add_child('fuel_and_transmission_type');
                var child2 = frm.add_child('other_details');
                child1.fuel_type = values.fuel_type;
                child1.transmission_type = values.transmission_type;
                child1.no_of_owners = values.no_of_owners;
                child1.index=child1.idx
                child2.fuel_type = values.fuel_type;
                child2.transmission_type = values.transmission_type;   
                child2.no_of_owners = values.no_of_owners;
                child2.index=child2.idx
                frm.refresh_fields('fuel_and_transmission_type');
                frm.refresh_fields('other_details');
                frm.set_value('length_of_child_tables', frm.doc.fuel_and_transmission_type.length + frm.doc.other_details.length);
            }, __('Add Field'));
        });
    },
    child_table_1_on_form_rendered: function(frm, cdt, cdn) {
        frm.fields_dict['fuel_and_transmission_type'].grid.on_grid_row_added = function(doc, cdt, cdn) {
            var child = locals[cdt][cdn];
            var child2 = frappe.model.add_child(cur_frm.doc, 'Other Details', 'other_details');
            child2.field1 = child.field1;
            child2.field2 = child.field2;
            child2.field3 = child.field3;
            cur_frm.refresh_fields('other_details');
            cur_frm.set_value('length_of_child_tables', cur_frm.doc.fuel_and_transmission_type.length + cur_frm.doc.other_details.length);
        };
        frm.fields_dict['fuel_and_transmission_type'].grid.on_grid_row_removed = function(doc, cdt, cdn) {
            var removed_row = locals[cdt][cdn];
            cur_frm.doc.other_details.forEach(function(row, index) {
                if (row.name === removed_row.name) {
                    cur_frm.doc.other_details.splice(index, 1);
                    cur_frm.refresh_field('other_details');
                    cur_frm.set_value('length_of_child_tables', cur_frm.doc.fuel_and_transmission_type.length + cur_frm.doc.other_details.length);
                    return false;
                }
            });
        };
    },
    child_table_2_on_form_rendered: function(frm, cdt, cdn) {
        frm.fields_dict['other_details'].grid.on_grid_row_added = function(doc, cdt, cdn) {
            var child = locals[cdt][cdn];
            var child1 = frappe.model.add_child(cur_frm.doc, 'Fuel and Transmission Type', 'fuel_and_transmission_type');
            child1.field1 = child.field1;
            child1.field2 = child.field2;
            child1.field3 = child.field3;
            cur_frm.refresh_fields('fuel_and_transmission_type');
            cur_frm.set_value('length_of_child_tables', cur_frm.doc.fuel_and_transmission_type.length + cur_frm.doc.other_details.length);
        };
        frm.fields_dict['other_details'].grid.on_grid_row_removed = function(doc, cdt, cdn) {
            var removed_row = locals[cdt][cdn];
            cur_frm.doc.fuel_and_transmission_type.forEach(function(row, index) {
                if (row.name === removed_row.name) {
                    cur_frm.doc.fuel_and_transmission_type.splice(index, 1);
                    cur_frm.refresh_field('fuel_and_transmission_type');
                    cur_frm.set_value('length_of_child_tables', cur_frm.doc.fuel_and_transmission_type.length + cur_frm.doc.other_details.length);
                    return false;
                }
            });
        };
    }
});

frappe.ui.form.on('Fuel and Transmission Type', {

});

frappe.ui.form.on('Other Details', {
    
    other_details_remove: function(frm) {
        frm.set_value("fuel_and_transmission_type",frm.doc.other_details)
        frm.refresh_field('fuel_and_transmission_type')
        frm.save()
}
});
