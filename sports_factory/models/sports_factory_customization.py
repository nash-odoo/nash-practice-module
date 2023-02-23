# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SportsFactoryCustomization(models.Model):
    _name = "sports.factory.customization"
    _description = "Sports Factory Customization Model"

    name = fields.Char()

    # _sql_constraints = [
    #     ('cust_id',
    #     'CHECK(customize_desc > 3)',
    #     'You can able to do max 3 customization!!')
    #     ]

    # @api.constrains('customize_desc')
    # def _check_customization(self):
    #     for record in self:
    #         if int(record.customize_desc) > 3:
    #             raise ValidationError("You can able to do max 3 customization!!")
