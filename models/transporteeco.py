
from odoo import fields, models, api


# MODELO TRANSPORTE
class TransporteEco(models.Model):
    _name = 'transporteeco.transporteeco'
    _description = 'transporteeco'
    _rec_name = 'transporte'
    transporte = fields.Selection([
        ('bicicleta', 'Bicicleta'),
        ('patinete', 'Patinete'),
        ('furgoneta_elec', 'Furgoneta Eléctrica')
    ], string=' Tipo de transporte',
        default='bicicleta',
        required=True,
        help='Elige el tipo de transporte deseado.')
    descripcion = fields.Text(' Descripción', required=True)
    envios = fields.One2many(
        comodel_name='envioeco.envioeco',
        inverse_name='tipo_transporte',
        string=' Envíos en el transporte')
    envios_resumen = fields.Char(string=' Resumen de envíos', compute='_compute_envios_resumen')
    estado_transporte = fields.Selection([
        ('en_almacen', 'En almacén'),
        ('en_reparto', 'En reparto')
    ], string='Estado del transporte', required=True, default='en_almacen')

    @api.depends('envios')
    def _compute_envios_resumen(self):
        for record in self:
            cantidad = len(record.envios)
            record.envios_resumen = f"{cantidad} envío{'s' if cantidad != 1 else ''}"

    _sql_constraints = [
        ('name_uniq', 'unique (transporte)', 'Este vehículo ya está asociado a uno o varios envíos' ),
    ]
    