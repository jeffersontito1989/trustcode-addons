# -*- coding: utf-8 -*-
# © 2017 Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


{  # pylint: disable=C8101,C8103
    'name': "Cadastro de Sites KK",

    'summary': """
        Cadastro de sites """,

    'description': """
        Cria o modelo para o cadastro de sites KK Engenharia
    """,
    'author': "Trustcode",
    'website': "http://www.trustcode.com.br",
    'category': 'Uncategorized',
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'contributors': [
        'Felipe Paloschi <paloschi.eca@gmail.com>',
    ],
    'depends': ['sale', 'project', 'purchase'],
    'data': [
        'views/kk_sites.xml',
        'views/kk_fabricante_torre.xml',
        'views/sale_order.xml',
        'views/project.xml',
        'views/purchase_order.xml',
        'security/ir.model.access.csv',
    ],
    'post_init_hook': 'post_init',

}