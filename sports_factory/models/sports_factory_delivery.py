# -*- coding: utf-8 -*-
from odoo import models, fields

class SportsFactoryDelivery(models.Model):
	_name = "sports.factory.delivery"
	_description = "Product Delivery"
	_order = "sequence"
	_rec_name = "state_group_id"

	state_group_id = fields.Char(required=True, string="Country Group")
	states_id = fields.Many2many('res.country.state', required=True)
	sequence = fields.Integer('sequence')
	delivery = fields.Char(required=True)
