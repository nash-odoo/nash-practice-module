# -*- coding: utf-8 -*-
from odoo import models, fields
from dateutil.relativedelta import relativedelta
from datetime import datetime


class SportsFactoryCategory(models.Model):
    _name = "sports.factory.category"
    _description = "Sports Factory Category Model"

    name = fields.Char(required=True)
    description = fields.Text()