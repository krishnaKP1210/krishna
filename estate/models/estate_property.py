from odoo import fields,models


class Estatetag(models.Model):
    _name = 'estate.tag'
    _description = 'estate property tag'

    name = fields.Char()


class Estateoffer(models.Model):
    _name = 'estate.offer'
    _description = 'estate offer'

    price = fields.Float()
    status = fields.Selection([('accepted' , 'Accepted'),('rejected','Rejected')])
    partner_id = fields.Many2one('res.partner')
    property_id = fields.Many2one('estate.property')


class Estatepropertytype(models.Model):
    _name = 'estate.property.type'
    _description = 'estate property type'


    name = fields.Char()


class Estateproperty(models.Model):
    _name = "estate.property"
    _description = "estate module for sales"
    
    
    name = fields.Char(string="Property Name", default="Unknown",required=True)
    description = fields.Text()
    selling_price = fields.Float(require=True)
    bedrom = fields.Integer(default=2)
    postcode = fields.Char()      
    date_availability  = fields.Date(default=lambda self: fields.Datetime.now() , copy=False) 
    expected_price = fields.Float(required=True)
    living_area  = fields.Integer()
    facades = fields.Integer()   
    garage = fields.Boolean()
    garden = fields.Boolean()          
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')       
        ])
    
    active = fields.Boolean(default=True)
    image = fields.Image()
    property_type_id = fields.Many2one('estate.property.type')
    property_tag_id = fields.Many2many('estate.tag')
    property_offer_id = fields.One2many('estate.offer','property_id')