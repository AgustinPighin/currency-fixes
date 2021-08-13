from odoo import models, api, fields, _
from odoo.exceptions import ValidationError
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError

class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

"""    print_curr_price_unit = fields.Float('Unit Price', required=True, digits='Product Price', default=0.0)

    print_curr_price_subtotal = fields.Float(compute='_compute_curr_amount', digits='Product Price', default=0.0, string='Subtotal', readonly=True, store=True)
    print_curr_price_tax      = fields.Float(compute='_compute_curr_amount', digits='Product Price', default=0.0, string='Total Tax', readonly=True, store=True)
    print_curr_price_total    = fields.Float(compute='_compute_curr_amount', digits='Product Price', default=0.0,  string='Total', readonly=True, store=True)"""

"""    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
    def _compute_curr_amount(self):

        print_currency_id = self.env['res.currency'].search([('name', '=', 'ARS')], limit=1)[0]

        for line in self:
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0) 
            taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_shipping_id)
            
            line.update({
                'print_curr_price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])) * print_currency_id.rate,
                'print_curr_price_total': taxes['total_included'] * print_currency_id.rate,
                'print_curr_price_subtotal': taxes['total_excluded'] * print_currency_id.rate ,
                'print_curr_price_unit' : line.price_unit * print_currency_id.rate, 
            })"""