# -*- coding: utf-8 -*-
from odoo import models, fields
from dateutil.relativedelta import relativedelta
from datetime import datetime


class SportsFactory(models.Model):
    _name = "sports.factory"
    _description = "Sports Factory Model"

    name = fields.Char(required=True)
    size = fields.Selection(
        string="Size",
        selection=[('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),
                   ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('s', 'S'),
                    ('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL') ])
    material = fields.Selection(
        string="Material",
        selection=[('sag', 'SAG'), ('english_willow', 'English Willow'),
                   ('wooden', 'Wooden'), ('leather', 'Leather'), ('rubber', 'Rubber')
                   ('kashmir_willow', 'Kashmir Willow'),('tennis', 'Tennis ')]) 
    colour = fields.Selection(
        string="Colour",
        selection=[('red', 'Red'), ('white', 'White'), ('blue', 'Blue'),
                   ('yellow', 'Yellow'), ('natural', 'Natural'),
                   ('multi_colour', 'Multi Colour')])  
    age_range = fields.Selection(
        string="Age",
        selection=[('<18', '<18'), ('>=18', '>=18'), ('anyone', 'Anyone')])       
    weight = fields.Float()
