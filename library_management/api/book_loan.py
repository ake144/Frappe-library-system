import frappe
from frappe.utils import nowdate

@frappe.whitelist()
def borrow_book(book_id, member_id, due_date):
    # Check if book exists
    book = frappe.get_doc("Book", book_id)
    if not book:
        return {"error": "Book not found"}
    
    # Check if book is already borrowed
    if book.status == "Borrowed":
        return {"error": "Book is already borrowed"}
    
    # Create a new book loan record
    loan = frappe.get_doc({
        "doctype": "Book Loan",
        "book_id": book.name,
        "member_id": member_id,
        "issue_date": nowdate(),
        "due_date": due_date,
        "status": "Borrowed"
    })
    loan.insert(ignore_permissions=True)

    # Update book status
    book.status = "Borrowed"
    book.save(ignore_permissions=True)
    frappe.db.commit()
    
    return {"message": "Book borrowed successfully"}

@frappe.whitelist()
def return_book(loan_id):
    # Get the loan record
    loan = frappe.get_doc("Book Loan", loan_id)
    if not loan:
        return {"error": "Loan record not found"}
    
    # Check if already returned
    if loan.status == "Returned":
        return {"error": "Book is already returned"}
    
    # Get the book and update its status
    book = frappe.get_doc("Book", loan.book_id)
    book.status = "Available"
    book.save(ignore_permissions=True)

    # Update loan record
    loan.return_date = nowdate()
    loan.status = "Returned"
    loan.save(ignore_permissions=True)
    frappe.db.commit()
    
    return {"message": "Book returned successfully"}
