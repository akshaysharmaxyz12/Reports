# # Copyright (c) 2024, akshay and contributors
# # For license information, please see license.txt
# import frappe
# from frappe import _
# from frappe.model.document import Document
# from frappe.utils import getdate, nowdate, now_datetime, get_datetime
# from frappe.model.document import Document


# @frappe.whitelist(allow_guest=True)
# def new_employee(data):
#     try:
#         new_employee = frappe.new_doc("Employee Detail")
#         new_employee.first_name = data.get("first_name")
#         new_employee.last_name = data.get("last_name")
#         new_employee.address = data.get("address")
#         new_employee.employee_id = data.get("employee_id")
#         new_employee.phone_no = data.get("phone_no")
#         new_employee.insert()
#         return new_employee
#     except Exception as e:
        # return str(e)



# @frappe.whitelist(allow_guest=True)
# def update_employee(data):
#     try:
#         if data.get("employee_detail_id"):
#             employee = frappe.get_doc("Employee Detail", data.get("employee_detail_id"))
#             if data.get("first_name"): 
#                 employee.first_name = data.get("first_name")
#             if data.get("last_name"): 
#                 employee.last_name = data.get("last_name")
#             if data.get("address"): 
#                 employee.address = data.get("address")
#             if data.get("employee_id"): 
#                 employee.employee_id = data.get("employee_id")
#             if data.get("phone_no"): 
#                 employee.phone_no = data.get("phone_no")
#             employee.save()
#             return employee
#     except Exception as e:
#         return str(e)
