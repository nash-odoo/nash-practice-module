# -*- coding: utf-8 -*-
from odoo import models, fields
from dateutil.relativedelta import relativedelta
from datetime import datetime


class SportsFactoryBrands(models.Model):
    _name = "sports.factory.brands"
    _description = "Sports Factory Brands Model"

    name = fields.Char(required=True)
    description = fields.Text()