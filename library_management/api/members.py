import frappe
from frappe.model.document import Document

# CREATE a new member
@frappe.whitelist(allow_guest=True)
def create_member(full_name, email, phone, membership_status="Active"):
    member = frappe.get_doc({
        "doctype": "Member",
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "membership_status": membership_status
    })
    member.insert(ignore_permissions=True)
    frappe.db.commit()
    return {"message": "Member created successfully", "member_id": member.name}

# READ member details
@frappe.whitelist(allow_guest=True)
def get_member(member_id):
    member = frappe.get_doc("Member", member_id)
    return member.as_dict()

# UPDATE member details
@frappe.whitelist(allow_guest=True)
def update_member(member_id, full_name=None, email=None, phone=None, membership_status=None):
    member = frappe.get_doc("Member", member_id)
    if full_name:
        member.full_name = full_name
    if email:
        member.email = email
    if phone:
        member.phone = phone
    if membership_status:
        member.membership_status = membership_status
    member.save()
    frappe.db.commit()
    return {"message": "Member updated successfully"}

# DELETE a member
@frappe.whitelist(allow_guest=True)
def delete_member(member_id):
    frappe.delete_doc("Member", member_id, ignore_permissions=True)
    frappe.db.commit()
    return {"message": "Member deleted successfully"}
