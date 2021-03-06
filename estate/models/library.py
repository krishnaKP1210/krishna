from odoo import models, fields

class Author(models.Model):
    _name = 'author'
    _description = 'Author'

    name = fields.Char()
    address = fields.Text()
    # book_id = fields.Many2one('books')

class BookCategory(models.Model):
    _name = 'book.category'
    _description = 'Book Category'

    name = fields.Char()

class BookDepartment(models.Model):
    _name = 'book.department'
    _description = 'Book Department'

    name = fields.Char()

class BookPublisher(models.Model):
    _name = 'book.publisher'
    _description = 'Book Publisher'

    name = fields.Char()




    
class Library(models.Model):
    _name = 'library.property'
    _description = 'Books'
    _sql_constraints = [('isbn_unique', 'unique(isbn)', 'Duplicate isbn not allowed')]


    name = fields.Char(string="book name", require=True)
    price = fields.Float()
    # author_ids = fields.One2many('author', 'book_id')
    author_ids = fields.Many2many('author')
    isbn = fields.Integer()
    category_id = fields.Many2one('book.category')
    department_id = fields.Many2one('book.department')
    barcode = fields.Char()
    publisher_id = fields.Many2one('book.publisher')
    edition = fields.Char() # Many 2 one 
    date = fields.Date()
    shelf_id = fields.Many2one('shelf')
