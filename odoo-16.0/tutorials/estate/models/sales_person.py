from odoo import fields, models


class SalesPerson(models.Model):
    _name = "estate.sales_person"
    _description = "A person who sells a property"

    name = fields.Char(required=True)
