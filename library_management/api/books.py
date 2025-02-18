import frappe
# from frappe.model.document import Document

# CREATE a new book
@frappe.whitelist(allow_guest=True)
def create_book(title, author, isbn, publish_date):
    book = frappe.get_doc({
        "doctype": "Book",
        "title": title,
        "author": author,
        "isbn": isbn,
        "publish_date": publish_date
    })
    book.insert(ignore_permissions=True)
    frappe.db.commit()
    return {"message": "Book created successfully", "book_id": book.name}

# READ book details
@frappe.whitelist(allow_guest=True)
def get_book(book_id):
    book = frappe.get_doc("Book", book_id)
    return book.as_dict()

# UPDATE book details
@frappe.whitelist(allow_guest=True)
def update_book(book_id, title=None, author=None, isbn=None, publish_date=None):
    book = frappe.get_doc("Book", book_id)
    if title:
        book.title = title
    if author:
        book.author = author
    if isbn:
        book.isbn = isbn
    if publish_date:
        book.publish_date = publish_date
    book.save()
    frappe.db.commit()
    return {"message": "Book updated successfully"}

# DELETE a book
@frappe.whitelist(allow_guest=True)
def delete_book(book_id):
    frappe.delete_doc("Book", book_id, ignore_permissions=True)
    frappe.db.commit()
    return {"message": "Book deleted successfully"}


@frappe.whitelist()
def get_available_books():
    books = frappe.get_all("Book" , filters={"status": "Available"},  fields=["name", "title", "author", "isbn"])  
    # filters={"status": "Available"}, 
    return books

