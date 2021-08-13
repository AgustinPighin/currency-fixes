##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import api, fields, models, _
from odoo.exceptions import RedirectWarning, UserError, ValidationError, AccessError
from odoo.tools import float_is_zero, float_compare, safe_eval, date_utils, email_split, email_escape_char, email_re
from odoo.tools.misc import formatLang, format_date, get_lang

from collections import defaultdict
from datetime import date, timedelta
from itertools import groupby
from itertools import zip_longest
from hashlib import sha256
from json import dumps

import json
import re

class AccountMove(models.Model):
    _inherit = 'account.move'

    report_currency_id = fields.Many2one("res.currency",  string="Currency", readonly=True, required=True )

#    def _get_currency_ars(self):
#        self.ensure_one()
#        """en header amount_tax/amount_total/amount_untaxed/currency_rate"""
#        report_currency_id =  self.env['res.currency'].search([('name', '=', 'ARS')], limit=1)[0]        
#        self.report_currency_id = report_currency_id


    def action_post(self):
        result = super(AccountMove, self).action_post()
        """en header amount_tax/amount_total/amount_untaxed/currency_rate"""
        report_currency_id =  self.env['res.currency'].search([('name', '=', 'ARS')], limit=1)[0]        
        self.report_currency_id = report_currency_id

        return result