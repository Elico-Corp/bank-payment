##############################################################################
#
#    Copyright (C) 2009 EduSense BV (<http://www.edusense.nl>).
#    All Rights Reserved
#
#    WARNING: This program as such is intended to be used by professional
#    programmers who take the whole responsability of assessing all potential
#    consequences resulting from its eventual inadequacies and bugs
#    End users who are looking for a ready-to-use solution with commercial
#    garantees and support are strongly adviced to contract EduSense BV
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Account Banking',
    'version': '0.68',
    'license': 'GPL-3',
    'author': 'EduSense BV',
    'website': 'http://www.edusense.nl',
    'category': 'Account Banking',
    'depends': ['account_banking'],
    'init_xml': [],
    'update_xml': [
        #'security/ir.model.access.csv',
    ],
    'demo_xml': [],
    'description': '''
    Module to import Dutch Multibank format transation files.

    This modules contains no logic, just an import filter for account_banking.
    ''',
    'active': False,
    'installable': True,
}
