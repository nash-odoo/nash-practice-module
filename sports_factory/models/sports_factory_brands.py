# -*- coding: utf-8 -*-
from odoo import models, fields

class SportsFactoryBrands(models.Model):
    _name = "sports.factory.brands"
    _description = "Sports Factory Brands Model"

    name = fields.Char(required=True)
    description = fields.Text()
    product_ids = fields.One2many("product.template", "brand_type")