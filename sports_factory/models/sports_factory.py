# -*- coding: utf-8 -*-
from odoo import models, fields
from dateutil.relativedelta import relativedelta
from datetime import datetime


class SportsFactory(models.Model):
    _name = "sports.factory"
    _description = "Sports Factory Model"

    name = fields.Char(required=True)
    description = fields.Text()
    product_image = fields.Binary()
    sports_type = fields.Many2one('sports.factory.category', string='Sport')
    brand_type = fields.Many2one('sports.factory.brands', string='Brand')
    price = fields.Float()
    size = fields.Selection(
        string="Size",
        selection=[('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),
                   ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('s', 'S'),
                    ('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL')])
    material = fields.Selection(
        string="Material",
        selection=[('sag', 'SAG'), ('english_willow', 'English Willow'), ('spandex', 'Spandex'),
                   ('wooden', 'Wooden'), ('leather', 'Leather'), ('rubber', 'Rubber'),
                   ('kashmir_willow', 'Kashmir Willow'),('tennis', 'Tennis '),('cotton', 'Cotton'),
                   ('pvc', 'PVC'), ('plastic', 'Plastic'), ('blend', 'Blend')]) 
    colour = fields.Selection(
        string="Colour",
        selection=[('red', 'Red'), ('white', 'White'), ('blue', 'Blue'),
                   ('yellow', 'Yellow'), ('natural', 'Natural'),('black', 'Black')])  
    age_range = fields.Selection(
        string="Age",
        selection=[('<18', '<18'), ('>=18', '>=18'), ('anyone', 'Anyone')])       
    weight = fields.Float()
    outer_material = fields.Selection(
        string="Outer Material",
        selection=[('polypropylene', 'Polypropylene'),
                   ('acrylonitrile_butadiene_styrene', 'Acrylonitrile Butadiene Styrene')]) 
