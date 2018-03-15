# -*- coding: utf-8 -*-
{
    'name': "algolia_ecommerce",

    'summary': """
        This module aim to add full test search support to the E-commerce""",

    'description': """
        Long description of module's purpose
    """,

    'author': 'Eng Mohamed Rabiea',
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Website',
    'version': '10.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','website_sale','website','website_field_autocomplete'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/res_config_settings_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}