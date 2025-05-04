
from odoo import fields, models, api
from odoo.exceptions import ValidationError


# MODELO ENVIOS
class EnvioEco(models.Model):
    _name = 'envioeco.envioeco'
    _description = 'envioeco'
    _rec_name = 'pedido'
    pedido = fields.Many2one(comodel_name='sale.order', required=True)
    direccion_entrega = fields.Char('Dirección de entrega', required=True)
    fecha_solicitud = fields.Date(string=' Fecha de solicitud', required=True, default=fields.Date.today)
    tipo_transporte = fields.Many2one(comodel_name='transporteeco.transporteeco', string=' Transporte del envío')
    fecha_entrega_prevista = fields.Date(string='Fecha de entrega prevista', required=True, default=fields.Date.today)
    estado = fields.Selection([
        ('pendiente_envio', 'Pendiente de envío'),
        ('en_reparto', 'En reparto'),
        ('entregado', 'Entregado'),
        ('no_entregado', 'No entregado')
    ], string=' Estado del envío',
        default='pendiente_envio',
        required=True,
        help='Selecciona el estado del envío.')
    fecha_entrega = fields.Date(string=' Fecha de entrega')
    from_transporte = fields.Boolean(string=' Desde transporte', default=False)

    @api.constrains('fecha_solicitud', 'fecha_entrega_prevista')
    def _check_fechas(self):
        for record in self:
            if record.fecha_solicitud and record.fecha_entrega_prevista:
                if record.fecha_solicitud > record.fecha_entrega_prevista:
                    raise ValidationError('La fecha de solicitud no puede ser posterior a la fecha de entrega prevista.')

    @api.constrains('pedido')
    def _check_pedido_unico(self):
        for record in self:
            if self.env['envioeco.envioeco'].search([('pedido', '=', record.pedido.id), ('id', '!=', record.id)], limit=1):
                raise ValidationError('Este pedido ya ha sido asignado a un transporte.')
    
    @api.model
    def create(self, vals):
        transporte_id = vals.get('tipo_transporte')
        if transporte_id:
            transporte = self.env['transporteeco.transporteeco'].browse(transporte_id)
            if transporte.estado_transporte == 'en_reparto':
                raise ValidationError("No se puede asignar un transporte que ya está en reparto.")
        was_from_transporte = vals.get('from_transporte')
        if was_from_transporte and not vals.get('tipo_transporte'):
            active_id = self.env.context.get('active_id')
            if active_id:
                vals['tipo_transporte'] = active_id
        envio = super(EnvioEco, self).create(vals)
        if was_from_transporte:
            envio.from_transporte = False
        return envio

    def write(self, vals):
        if 'tipo_transporte' in vals:
            transporte = self.env['transporteeco.transporteeco'].browse(vals['tipo_transporte'])
            if transporte.estado_transporte == 'en_reparto':
                raise ValidationError("No se puede asignar un transporte que ya está en reparto.")
        return super(EnvioEco, self).write(vals)

