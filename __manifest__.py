# -*- coding: utf-8 -*-
{
    'name': "EcoDelivery",

    'summary': 'Eco-friendly delivery management for urban logistics',

    'description': """
        EcoDelivery is a module designed to manage sustainable last-mile delivery services.
        It allows businesses to plan and control delivery routes using bicycles or electric vehicles,
        assign orders to drivers, monitor delivery times, and reduce environmental impact.
    """,

    'author': "Samuel Mateos Tovar",
    'website': "https://github.com/svmmydev",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}