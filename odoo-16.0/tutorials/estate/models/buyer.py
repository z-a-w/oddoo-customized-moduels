from odoo import fields, models


class Buyer(models.Model):
    _name = "estate.buyer"
    _description = "A person who buy a property"

    name = fields.Char(required=True)
