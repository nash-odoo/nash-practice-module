# # -*- coding: utf-8 -*-
# from odoo import models, fields, api

# class SportsFactory(models.Model):
#     _name = "sports.factory"
#     _description = "Sports Factory Model"
#     _inherits ={'product.product':'product_id'} 

#     _sql_constraints = [
#     ('check_price','CHECK(price>0)','Price must be postivie!!')]

#     name = fields.Char(required=True)
#     description = fields.Text()
#     product_image = fields.Binary()
#     category_type = fields.Many2one('sports.factory.product.category', string="category")
#     sports_type = fields.Many2one('sports.factory.category', string='Sport')
#     brand_type = fields.Many2one('sports.factory.brands', string='Brand')
#     base_price = fields.Float(compute="_compute_discount", readonly=False, store=True)
#     price = fields.Float()
#     price_store = fields.Float()
#     offer_available = fields.Boolean()
#     five_percent_offer = fields.Boolean()
#     ten_percent_offer = fields.Boolean()
#     twenty_percent_offer = fields.Boolean()
#     # discounted_price = fields.Float(readonly=True)
#     countable = fields.Boolean()
#     int_size = fields.Selection(
#         string="Size(Numbers)",
#         selection=[('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),
#                    ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])
#     char_size = fields.Selection(
#         string="Size(Character)",
#         selection=[('s', 'S'),('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL')])
#     material = fields.Selection(
#         string="Material",
#         selection=[('sag', 'SAG'), ('english_willow', 'English Willow'), ('spandex', 'Spandex'),
#                    ('wooden', 'Wooden'), ('leather', 'Leather'), ('rubber', 'Rubber'),
#                    ('kashmir_willow', 'Kashmir Willow'),('tennis', 'Tennis '),('cotton', 'Cotton'),
#                    ('pvc', 'PVC'), ('plastic', 'Plastic'), ('blend', 'Blend')]) 
#     colour = fields.Selection(
#         string="Colour",
#         selection=[('red', 'Red'), ('white', 'White'), ('blue', 'Blue'),
#                    ('yellow', 'Yellow'), ('natural', 'Natural'),('black', 'Black')])  
#     age_range = fields.Selection(
#         string="Age",
#         selection=[('<18', '<18'), ('>=18', '>=18'), ('anyone', 'Anyone')])       
#     weight = fields.Float()
#     outer_material = fields.Selection(
#         string="Outer Material",
#         selection=[('polypropylene', 'Polypropylene'),
#                    ('acrylonitrile_butadiene_styrene', 'Acrylonitrile Butadiene Styrene')]) 
#     customization_ids = fields.Many2many('sports.factory.customization')
#     extra_cost = fields.Integer(compute="_compute_extra_cost", store=True)
#     state = fields.Selection(
#         selection=[('in stock','IN STOCK'),('out of stock','OUT OF STOCK'),('done','Done'),('published','Published')],
#         default='in stock')
#     total_price = fields.Integer(readonly=True)
#     state_group_id = fields.Many2one('sports.factory.delivery')
#     states_id = fields.Many2many('res.country.state',compute="_compute_state_id")
#     # state_id = fields.Many2one('res.country.state',string="State",domain="[('id', 'in', states_id)]")
#     delivery_time = fields.Char(related="state_group_id.delivery")
#     product_id = fields.Many2one('product.template', required=True, ondelete="cascade")

#     def action_done(self):
#         self.state = "done"

#     def action_publish(self):
#         self.state = "published"

#     @api.depends("price","customization_ids")
#     def _compute_extra_cost(self):
#         for record in self:
#             if record.customization_ids:
#                 record.extra_cost = len(record.mapped("customization_ids"))*100
#                 record.total_price = record.price + record.extra_cost
#             else:
#                 record.total_price = record.price
#                 record.extra_cost = 0

#     @api.depends("price","offer_available","five_percent_offer","ten_percent_offer","twenty_percent_offer")
#     def _compute_discount(self):
#         for record in self:
#             # breakpoint()
#             record.price_store = record.price
#             # breakpoint()
#             if record.offer_available:
#                 if record.five_percent_offer:
#                     record.base_price = record.price * 0.05
#                     # record.discounted_price = record.price * 0.5
#                     record.price = record.price - record.base_price
#                     record.total_price = record.price + record.extra_cost
#                 elif record.ten_percent_offer:
#                     record.base_price = record.price * 0.1
#                     # record.discounted_price = record.price * 0.10
#                     record.price = record.price - record.base_price
#                     record.total_price = record.price + record.extra_cost
#                 elif record.twenty_percent_offer:
#                     record.base_price = record.price * 0.2
#                     # record.discounted_price = record.price * 0.20
#                     record.price = record.price - record.base_price
#                     record.total_price = record.price + record.extra_cost
#                 else:
#                     record.price = record.price_store
#                     record.base_price = 0
#             else:
#                 record.price = record.price_store
#                 record.base_price = 0
#             # else:
#             #     # breakpoint()
#             #     record.total_price = record.price + record.extra_cost

#     @api.depends('state_group_id')
#     def _compute_state_id(self):
#         for record in self:
#             record.states_id = record.state_group_id.mapped('states_id')