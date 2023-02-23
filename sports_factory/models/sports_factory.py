# -*- coding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime


class SportsFactory(models.Model):
    _name = "sports.factory"
    _description = "Sports Factory Model"

    _sql_constraints = [
    ('check_price','CHECK(price>0)','Price must be postivie!!')]

    name = fields.Char(required=True)
    description = fields.Text()
    product_image = fields.Binary()
    category_type = fields.Many2one('sports.factory.product.category', string="category")
    sports_type = fields.Many2one('sports.factory.category', string='Sport')
    brand_type = fields.Many2one('sports.factory.brands', string='Brand')
    price = fields.Float()
    int_size = fields.Selection(
        string="Size(Numbers)",
        selection=[('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),
                   ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])
    char_size = fields.Selection(
        string="Size(Character)",
        selection=[('s', 'S'),('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL')])
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
    weight = fields.Float(readonly=True)
    outer_material = fields.Selection(
        string="Outer Material",
        selection=[('polypropylene', 'Polypropylene'),
                   ('acrylonitrile_butadiene_styrene', 'Acrylonitrile Butadiene Styrene')]) 
    customization_ids = fields.Many2many('sports.factory.customization')
    extra_cost = fields.Integer(compute="_compute_extra_cost")
    state = fields.Selection(
        selection=[('manufacturing','Manufacturing'),('packaging','Packaging'),
        ('delivered','Delivered'),('done','Done')])
    total_price = fields.Integer(readonly=True)

    def action_done(self):
        self.state = "done"

    @api.depends("customization_ids")
    def _compute_extra_cost(self):
        for record in self:
            if record.customization_ids:
                record.extra_cost = len(record.mapped("customization_ids"))*100
                record.total_price = record.price + record.extra_cost
            else:
                record.total_price = record.price
                record.extra_cost = 0