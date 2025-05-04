
from odoo import fields, models


class TransporteEco(models.Model):
    _name = 'transporteeco.transporteeco'
    _description = 'transporteeco'
    _rec_name = 'transporte'
    transporte = fields.Selection([
        ('bicicleta', 'Bicicleta'),
        ('patinete', 'Patinete'),
        ('furgoneta_elec', 'Furgoneta Eléctrica')
    ], string='Tipo de transporte',
        default='bicicleta',
        required=True,
        help='Elige el tipo de transporte deseado.')
    descripcion = fields.Char('Descripción', required=True)
    envios = fields.One2many(
        comodel_name='envioeco.envioeco',
        inverse_name='tipo_transporte',
        string='Envíos en el transporte')

    _sql_constraints = [
        ('name_uniq', 'unique (transporte)', '¡Transporte ya existente!' ),
    ]
    