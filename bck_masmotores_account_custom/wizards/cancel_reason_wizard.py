# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class CancelReasonWizard(models.TransientModel):
    _name = 'cancel.reason.wizard'
    _description = "Select Cancellation Reason"

    move_id = fields.Many2one('account.move', string="Invoice", required=True)
    cancellation_reason = fields.Selection(
        selection=lambda self: self._get_reasons(),
        string="Cancellation Reason",
        required=True
    )

    def _get_reasons(self):
        self.ensure_one()
        if not self.move_id:
            return []
        # Usamos el diario para determinar cliente/proveedor
        journal_type = self.move_id.journal_id.type
        if journal_type in ('sale', 'sale_refund'):
            tipo = 'cliente'
        else:
            tipo = 'proveedor'
        return [(code, desc) for code, desc, t in self.move_id.CANCELLATION_REASONS if t == tipo]

    def action_confirm_cancel(self):
        if not self.cancellation_reason:
            raise UserError("Debe seleccionar un motivo de cancelación.")
        self.move_id.cancellation_reason = self.cancellation_reason
        # Ejecutamos cancelación real
        self.move_id.button_draft() if self.move_id.state == 'posted' else None
        self.move_id.button_cancel()
        return {'type': 'ir.actions.act_window_close'}