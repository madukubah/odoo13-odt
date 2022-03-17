# -*- coding: utf-8 -*-

from odoo import fields, models, api, _



class ResCompany(models.Model):
    _inherit = "res.company"

    allowed_discrepancy = fields.Float(string='Allowed % Discrepancy from PO for Vendor Bill', default=5.0)