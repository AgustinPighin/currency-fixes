##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Invoice Print Ars',
    'version': '13.0.1.1.2',
    'category': 'Accounting',
    'sequence': 14,
    'author': 'Agustin Pighin',
    'website': 'www.agustinpighin.com.ar',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        'account',
    ],
    'data': [
        'views/report_invoice_fe_x.xml',
        'views/report_invoice_fe_x_qr.xml',
        'views/report_invoice_fe_ars.xml',
        'views/report_invoice_fe_ars_qr.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
