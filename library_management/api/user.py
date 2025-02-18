import frappe

def create_member_on_user_creation(doc, method):
    if not frappe.db.exists("Member", {"user": doc.name}):
        member = frappe.get_doc({
            "doctype": "Member",
            "full_name": doc.full_name or doc.first_name,
            "user": doc.name
        })
        member.insert()
