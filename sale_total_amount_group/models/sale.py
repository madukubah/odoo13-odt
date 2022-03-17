from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    consumable_amount = fields.Float('Consumable Total',
                                    compute='get_sub_amount', default=0)
    service_amount = fields.Float('Service Total',
                                    compute='get_sub_amount', default=0)
    stockable_amount = fields.Float('Stockable Product Total',
                                    compute='get_sub_amount', default=0)

    is_consumable_exist = fields.Boolean('Consumable exists',
                                    compute='get_sub_amount', default=False)
    is_service_exist = fields.Boolean('Service exists',
                                    compute='get_sub_amount', default=False)
    is_stockable_exist = fields.Boolean('Service exists',
                                    compute='get_sub_amount', default=False)

    @api.depends('order_line')
    def get_sub_amount(self):
        for record in self:
            orderlines = record.order_line
            
            record.consumable_amount = sum([x.price_total for x in orderlines if x.product_id.type == "consu" ])
            record.service_amount = sum([x.price_total for x in orderlines if x.product_id.type == "service" ])
            record.stockable_amount = sum([x.price_total for x in orderlines if x.product_id.type == "product" ])

            record.is_consumable_exist = sum([1 for x in orderlines if x.product_id.type == "consu" ]) > 0 
            record.is_service_exist = sum([1 for x in orderlines if x.product_id.type == "service" ]) > 0
            record.is_stockable_exist = sum([1 for x in orderlines if x.product_id.type == "product" ]) > 0 
