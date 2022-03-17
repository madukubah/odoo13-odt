# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.onchange('price_unit')
    def _check_allowed_discrepancy(self):
        for line in self:
            if( line.move_id.type == 'in_invoice' ):
                if(line.purchase_line_id) : 
                    allowed_discrepancy = self.company_id.allowed_discrepancy
                    threshold = line.purchase_line_id.price_unit * allowed_discrepancy / 100
                    product_price = line.purchase_line_id.price_unit

                    if(
                        not (
                            line.price_unit - threshold <= product_price and
                            product_price  <= line.price_unit + threshold
                        )
                    ):
                        raise UserError(_('You are not allowed to change the price exceeding the Allowed Discrepancy .') )
                    

