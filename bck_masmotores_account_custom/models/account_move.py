from odoo import models, api

class AccountMove(models.Model):
    _inherit = "account.move"

    @api.multi
    def action_invoice_print(self):
        """
        Reemplaza dinámicamente el formato de impresión según la empresa.
        Si la factura pertenece a una empresa específica, usa un reporte especial.
        """
        self.ensure_one()

        # Reemplaza este XML ID por el de tu empresa específica
        company_especial = self.env.ref("base.main_company")  # Ejemplo: Kiblo Caps Co.

        if self.company_id.id == company_especial.id:
            # Usar formato estándar
            return self.env.ref("account.account_invoices").report_action(self)
        else:
            # Usar formato personalizado
            return self.env.ref("prueba.report_invoice_company2").report_action(self)