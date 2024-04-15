# Copyright (c) 2024, akshay and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ErrorLogTask(Document):
    def validate(self):
        try:
            if not self.get("phone_no", "").startswith('+'):
                raise ValueError("Invalid mobile number format")
        except ValueError as e:
            error_message = f"Error in {self.doctype}: {e}"
            frappe.msgprint("Error: " + str(e), title="Validation Error")
            frappe.log_error(error_message)

