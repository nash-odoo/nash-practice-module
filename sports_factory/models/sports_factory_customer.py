# -*- coding: utf-8 -*-
from odoo import models, fields
from dateutil.relativedelta import relativedelta
from datetime import datetime


class SportsFactoryCustomer(models.Model):
    _name = "sports.factory.customer"
    _description = "Sports Factory Customer Model"

    name = fields.Char(required=True)
    description = fields.Text()