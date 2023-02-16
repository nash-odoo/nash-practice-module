# -*- coding: utf-8 -*-
from odoo import models, fields

class SportsFactoryProductCategory(models.Model):
    _name = "sports.factory.product.category"
    _description = "Sports Factory Product Category Model"

    name = fields.Char(required=True)
    sports_type = fields.Many2one('sports.factory.category', string='Sport')