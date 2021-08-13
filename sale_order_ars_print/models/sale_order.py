from odoo import models, api, fields, _
from odoo.exceptions import ValidationError
from odoo.tools.misc import formatLang, get_lang
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare
from datetime import datetime, timedelta
from functools import partial
from itertools import groupby


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    print_curr_amount_untaxed = fields.Monetary(string='Untaxed Amount', store=True, readonly=True, compute='_amount_curr_all', tracking=True)
    print_curr_amount_tax     = fields.Monetary(string='Taxes', store=True, readonly=True, compute='_amount_curr_all')
    print_curr_amount_total   = fields.Monetary(string='Total', store=True, readonly=True, compute='_amount_curr_all')
    print_currency_id         = fields.Many2one("res.currency",  string="Currency", readonly=True, required=True,compute='_get_currency')
    amount_by_group_curr      = fields.Binary(string="Tax amount by group", help="type: [(name, amount, base, formated amount, formated base)]")

    print_currency_rate       = fields.Float(copy=False, digits=(16, 6), readonly=True, string="Currency Rate")

    #print_currency_id = fields.Many2one("res.currency", related='pricelist_id.currency_id', string="Currency", readonly=True, required=True)

    def _get_currency(self):
        self.ensure_one()
        """en header amount_tax/amount_total/amount_untaxed/currency_rate"""
        print_currency_id  =  self.env['res.currency'].search([('name', '=', 'ARS')], limit=1)[0]        
        self.print_currency_id  = print_currency_id 

"""    def action_cancel(self):
        return super().action_cancel() """

"""    def action_quotation_sent(self):
        self._amount_curr_all()
        return super().action_quotation_sent()"""

"""      @api.depends('order_line.price_total')
    def _amount_curr_all(self):

        print_currency_id = self.env['res.currency'].search([('name', '=', 'ARS')], limit=1)[0]

        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax

            print_curr_amount_untaxed = amount_untaxed * print_currency_id.rate
            print_curr_amount_tax     = amount_tax * print_currency_id.rate
            print_curr_amount_total   = amount_untaxed + amount_tax
            print_curr_amount_total   = print_curr_amount_total * print_currency_id.rate

            order.update({
                'print_curr_amount_untaxed': print_curr_amount_untaxed,
                'print_curr_amount_tax': print_curr_amount_tax,
                'print_curr_amount_total': print_curr_amount_total,
                'print_currency_rate': print_currency_id.rate,
                'print_currency_id': print_currency_id,
            })"""  

"""    def _amount_by_group_curr(self):
        for order in self:
            currency = self.env['res.currency'].search([('name', '=', 'ARS')], limit=1)[0]
            fmt = partial(formatLang, self.with_context(lang=order.partner_id.lang).env, currency_obj=currency)
            res = {}
            for line in order.order_line:
                price_reduce = line.price_unit * (1.0 - line.discount / 100.0) * currency.rate
                taxes = line.tax_id.compute_all(price_reduce, quantity=line.product_uom_qty, product=line.product_id, partner=order.partner_shipping_id)['taxes']
                for tax in line.tax_id:
                    group = tax.tax_group_id
                    res.setdefault(group, {'amount': 0.0, 'base': 0.0})
                    for t in taxes:
                        if t['id'] == tax.id or t['id'] in tax.children_tax_ids.ids:
                            res[group]['amount'] += t['amount']
                            res[group]['base'] += t['base']
            res = sorted(res.items(), key=lambda l: l[0].sequence)
            order.amount_by_group_curr = [(
                l[0].name, l[1]['amount'], l[1]['base'],
                fmt(l[1]['amount']), fmt(l[1]['base']),
                len(res),
            ) for l in res]  """