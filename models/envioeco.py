
from odoo import fields, models, api
from odoo.exceptions import ValidationError


# MODELO TRANSPORTE ECO
class EnvioEco(models.Model):
    _name = 'envioeco.envioeco'
    _description = 'envioeco'
    _rec_name = 'pedido'
    pedido = fields.Many2one(comodel_name='sale.order', required=True)
    direccion_entrega = fields.Char('Dirección de entrega', required=True)
    fecha_solicitud = fields.Date(string='Fecha de solicitud', required=True, default=fields.Date.today)
    tipo_transporte = fields.Many2one(comodel_name='transporteeco.transporteeco', string='Transporte del envío')
    fecha_entrega_prevista = fields.Date(string='Fecha de entrega prevista', required=True, default=fields.Date.today)
    estado = fields.Selection([
        ('pendiente_envio', 'Pendiente de envío'),
        ('en_reparto', 'En reparto'),
        ('entregado', 'Entregado'),
        ('no_entregado', 'No entregado')
    ], string='Estado del envío',
        default='pendiente_envio',
        required=True,
        help='Selecciona el estado del envío.')
    fecha_entrega = fields.Date(string='Fecha de entrega')

    @api.constrains('fecha_solicitud', 'fecha_entrega_prevista')
    def _check_fechas(self):
        for record in self:
            if record.fecha_solicitud and record.fecha_entrega_prevista:
                if record.fecha_solicitud > record.fecha_entrega_prevista:
                    raise ValidationError('La fecha de solicitud no puede ser posterior a la fecha de entrega prevista.')
    