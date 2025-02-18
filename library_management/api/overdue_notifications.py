import frappe
from frappe.utils import nowdate

def send_overdue_reminders():
    today = nowdate()
    
    overdue_loans = frappe.get_all(
        "Book Loan",
        filters={"due_date": ["<", today], "status": "Borrowed"},
        fields=["name", "member_id", "book_id", "due_date"]
    )

    for loan in overdue_loans:
        member = frappe.get_doc("Library Member", loan.member_id)
        book = frappe.get_doc("Book", loan.book_id)

        frappe.sendmail(
            recipients=[member.email],
            subject=f"Overdue Book Reminder: {book.title}",
            message=f"Dear {member.member_name},<br><br>"
                    f"The book <b>{book.title}</b> was due on <b>{loan.due_date}</b> and is now overdue.<br>"
                    f"Please return it as soon as possible to avoid penalties.<br><br>"
                    f"Thank you!"
        )

    frappe.db.commit()
