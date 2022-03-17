from odoo import models, fields, api, _


class purchase_order(models.Model):
    _inherit = "purchase.order"


    time_of_delivery = fields.Float('Time of Delivery (days)',
                                    compute='get_time_of_delivery')

    @api.depends('date_planned', 'date_order')
    def get_time_of_delivery(self):
        for record in self:
            if not record.date_planned:
                record.date_planned = fields.Date.today()
            mpd = fields.Date.from_string(record.date_planned)
            do = fields.Date.from_string(record.date_order)
            tod = mpd - do
            record.time_of_delivery = tod.days
