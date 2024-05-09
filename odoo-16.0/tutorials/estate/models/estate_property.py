from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "House and properties"

    name = fields.Char(required=True)
    description = fields.Text()
    post_code = fields.Char()
    date_availability = fields.Date(copy=False, default=fields.Datetime.add(fields.Datetime.today(), month=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string='Orientation', selection=[
        ('north', 'North'),
        ('east', 'East'),
        ('south', 'South'),
        ('west', 'West')
    ])
    active = fields.Boolean(default=True)
    state = fields.Selection(string='State', selection=[
        ('new', 'New'),
        ('offer', 'Offer'),
        ('received', 'Received'),
        ('offer_accepted', 'Offer Accepted')
    ])

