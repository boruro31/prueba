from odoo import models, fields, api
from odoo.exceptions import UserError
class AccountMove(models.Model):
    _inherit = 'account.move'

    def button_open_cancel_wizard(self):
        return {
            'name': "Motivo de Cancelación",
            'type': 'ir.actions.act_window',
            'res_model': 'cancel.reason.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_move_id': self.id},
        }