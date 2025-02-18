import frappe

def redirect_after_login(login_manager):
    frappe.local.response["home_page"] = "/available-books"
