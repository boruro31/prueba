# -*- coding: utf-8 -*-
{
    "name": " Bck MasMotores Account Custom",
    "summary": """Invoice Branding for MasMotores Modules
    """,
    "description": """Generate invoice format and menu to select the reasons for invoice cancellation
    """,
    "author": "Abraham Sanchez_Becken",
    "support": "contacto@becken.mx",
    "website": "http://www.becken.mx",
    "company": "Becken",
    "maintainer": " Abraham Sanchez_Becken",
    "license": "OPL-1",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/17.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Account",
    "version": "18.0.0.1",
    # any module necessary for this one to work correctly
    "depends": [
        'account',
    ],
    # always loaded
    "data": [
        'reports/report_actions.xml',
        'reports/report_invoice_company2.xml',
    ],
} 