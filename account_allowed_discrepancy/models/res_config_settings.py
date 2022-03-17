# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    allowed_discrepancy = fields.Float(string='Allowed % Discrepancy from PO for Vendor Bill', related='company_id.allowed_discrepancy', readonly=False )
    # allowed_discrepancy = fields.Float(string='Allowed % Discrepancy from PO for Vendor Bill', default=5.0)
