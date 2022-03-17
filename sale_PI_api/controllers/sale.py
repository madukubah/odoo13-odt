from odoo import http
from odoo.http import request
from werkzeug.wrappers import Request, Response
import json
import logging
_logger = logging.getLogger(__name__)

class SalePIController(http.Controller):

    @http.route('/sale-pi/', auth='public', methods=['GET'], csrf=False)
    def index(self):
        try:
            sale_orders = request.env['sale.order'].sudo().search([])
        except:
            return 'cannot access API'
        data = [{
               "id": sale_order.id,
               "pi_sale_id": sale_order.pi_sale_id or False,
                "name": sale_order.name ,
                "customer": sale_order.partner_id.name ,
                "date_order": sale_order.date_order.strftime("%m/%d/%Y, %H:%M:%S") ,
                "state": sale_order.state
            } for sale_order in sale_orders ]

        headers = {
            'Content-Type': 'application/json',
            }
        body = data

        return Response(json.dumps(body), headers=headers, status = 200)

    @http.route('/sale-pi/', auth='public', methods=['POST'], csrf=False)
    def post(self, **post):
        SaleOrder = request.env['sale.order'].sudo()

        try:
            sale_order = SaleOrder.search([
                ('pi_sale_id', '=', post['pi_sale_id'] )
            ], limit = 1)

            if sale_order: 
                raise Exception("duplicate PI id")

            sale_order = SaleOrder.create({
                'pi_sale_id': post['pi_sale_id'],
                'partner_id': int(post['partner_id'])
                })
        except Exception as e:
            headers = {
                'Content-Type': 'application/json',
            }
            return Response(json.dumps(str(e)), headers=headers, status = 409)
        
        headers = {
            'Content-Type': 'application/json',
            }

        body = {
            'id': sale_order.id
        }

        return Response(json.dumps(body), headers=headers, status = 200)

    @http.route('/sale-pi/', auth='public', methods=['DELETE'], csrf=False)
    def delete(self, **post):
        SaleOrder = request.env['sale.order'].sudo()

        try:
            sale_order = SaleOrder.search([
                ('pi_sale_id', '=', post['pi_sale_id'] )
            ], limit = 1)

            if not sale_order: 
                raise Exception("PI id not found")
            
            sale_order.unlink()
        except Exception as e:
            headers = {
                'Content-Type': 'application/json',
            }
            return Response(json.dumps(str(e)), headers=headers, status = 409)
        
        headers = {
            'Content-Type': 'application/json',
            }

        return Response(json.dumps("successfully deleted"), headers=headers, status = 200)

    @http.route('/sale-pi/', auth='public', methods=['PATCH'], csrf=False)
    def patch(self, **post):
        SaleOrder = request.env['sale.order'].sudo()

        try:
            sale_order = SaleOrder.search([
                ('pi_sale_id', '=', post['pi_sale_id'] )
            ], limit = 1)

            if not sale_order: 
                raise Exception("PI id not found")

            sale_order.write({
                    'partner_id': int(post['partner_id'])
                })
        except Exception as e:
            headers = {
                'Content-Type': 'application/json',
            }
            return Response(json.dumps(str(e)), headers=headers, status = 409)
        
        headers = {
            'Content-Type': 'application/json',
            }

        body = {
            'id': sale_order.id
        }

        return Response(json.dumps(body), headers=headers, status = 200)

    @http.route('/sale-pi/confirm', auth='public', methods=['POST'], csrf=False)
    def confirm(self, **post):
        SaleOrder = request.env['sale.order'].sudo()

        try:
            sale_order = SaleOrder.search([
                ('pi_sale_id', '=', post['pi_sale_id'] )
            ], limit = 1)

            if not sale_order: 
                raise Exception("PI id not found")
            
            sale_order.action_confirm()
        except Exception as e:
            headers = {
                'Content-Type': 'application/json',
            }
            return Response(json.dumps(str(e)), headers=headers, status = 409)
        
        headers = {
            'Content-Type': 'application/json',
            }

        body = {
            'id': sale_order.id
        }

        return Response(json.dumps(body), headers=headers, status = 200)

    @http.route('/sale-pi/cancel', auth='public', methods=['POST'], csrf=False)
    def cancel(self, **post):
        SaleOrder = request.env['sale.order'].sudo()

        try:
            sale_order = SaleOrder.search([
                ('pi_sale_id', '=', post['pi_sale_id'] )
            ], limit = 1)

            if not sale_order: 
                raise Exception("PI id not found")
            
            sale_order.action_cancel()
        except Exception as e:
            headers = {
                'Content-Type': 'application/json',
            }
            return Response(json.dumps(str(e)), headers=headers, status = 409)
        
        headers = {
            'Content-Type': 'application/json',
            }

        body = {
            'id': sale_order.id
        }

        return Response(json.dumps(body), headers=headers, status = 200)

    @http.route('/sale-pi/draft', auth='public', methods=['POST'], csrf=False)
    def draft(self, **post):
        SaleOrder = request.env['sale.order'].sudo()

        try:
            sale_order = SaleOrder.search([
                ('pi_sale_id', '=', post['pi_sale_id'] )
            ], limit = 1)

            if not sale_order: 
                raise Exception("PI id not found")
            
            sale_order.action_draft()
        except Exception as e:
            headers = {
                'Content-Type': 'application/json',
            }
            return Response(json.dumps(str(e)), headers=headers, status = 409)
        
        headers = {
            'Content-Type': 'application/json',
            }
        body = {
            'id': sale_order.id
        }

        return Response(json.dumps(body), headers=headers, status = 200)

    