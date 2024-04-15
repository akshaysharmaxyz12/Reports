# Copyright (c) 2024, akshay and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document
# from frappe import _


# class CustomerDetail(Document):
# 	pass


# def encrypt_aadhar_card_number(doc, method):

#     if doc.aadhar_card_number and not frappe.db.get_value(doc.doctype, doc.name, 'encrypted_aadhar_card_number'):
#         encrypted_aadhar_card_number = frappe.encrypt(doc.aadhar_card_number)
#         doc.encrypted_aadhar_card_number = encrypted_aadhar_card_number



# In your_custom_app/custom_app/doctype/customer_detail/customer_detail.py

import frappe
from frappe.model.document import Document
from cryptography.fernet import Fernet

key = Fernet.generate_key()

print("Generated Key:", key)

encoded_key = key.decode()

cipher_suite = Fernet(encoded_key)

class CustomerDetail(Document):
    def before_save(self):
        if self.aadhar_card_number:
            encrypted_aadhar = encrypt(self.aadhar_card_number)
            self.aadhar_card_number = encrypted_aadhar

def encrypt(value):
    encrypted_value = cipher_suite.encrypt(value.encode())
    return encrypted_value

def decrypt(encrypted_value):
    decrypted_value = cipher_suite.decrypt(encrypted_value).decode()
    return decrypted_value


