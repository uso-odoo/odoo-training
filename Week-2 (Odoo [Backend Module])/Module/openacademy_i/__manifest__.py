# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,
    'maintainer': 'Tiny ERP Pvt. Lmt.',
    'company': 'Tiny ERP Pvt. Lmt.',

    'author': "Urvi Soni",
    'website': "https://urvisoni.github.io/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # 'depends': ['base','sale'],
    'depends': ['base', 'openacademy'],


    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'templates.xml',
        # 'views/openacademy.xml',
        # 'views/partner.xml',
        # 'views/session_board.xml',
        'views/demo.xml'
        # 'reports.xml',

    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo.xml',
    # ],
}
