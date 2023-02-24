# -*- coding: utf-8 -*-
from odoo import models, fields

class SportsFactoryCategory(models.Model):
    _name = "sports.factory.category"
    _description = "Sports Factory Category Model"

    name = fields.Char(required=True)
    description = fields.Text()
    product_ids = fields.One2many("sports.factory", "sports_type")