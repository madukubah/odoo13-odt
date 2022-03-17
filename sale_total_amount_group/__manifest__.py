{
    'name': 'Sale Total Amount Grouping',
    'version': '1.0',
    'depends': ['sale', 'sale_management', 'stock'],
    'author': 'Muhammad Alfalah Madukubah',
    'description': """
        Show Subtotal Amount in Group By Product Type
    """,
    'website': 'http://www.portcities.net',
    'category': 'Sale',
    'sequence': 1,
    'data': [
        'views/sale_view.xml'
        ],
    'auto_install': False,
    'installable': True,
    'application': False,
}
