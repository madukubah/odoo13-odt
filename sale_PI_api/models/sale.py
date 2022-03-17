from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    pi_sale_id = fields.Char('PI reference', unique=True)
    