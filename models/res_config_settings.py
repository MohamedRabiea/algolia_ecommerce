from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    application_id = fields.Char('Application ID', require=True)
    search_key = fields.Char('Search Only API Key', require=True)
    admin_key = fields.Char('Admin API Key')
    menitor_key = fields.Char('Monitoring API Key')

    def set_application_id(self):
        self.env['ir.config_parameter'].set_param('algolia_ecommerce.application_id',
                                                  (self.application_id or '').strip())

    def get_default_application_id(self, fields):
        application_id = self.env['ir.config_parameter'].get_param('algolia_ecommerce.application_id', default='')
        return dict(application_id=application_id)

    def set_search_key(self):
        self.env['ir.config_parameter'].set_param('algolia_ecommerce.search_key', (self.search_key or '').strip())

    def get_default_search_key(self, fields):
        search_key = self.env['ir.config_parameter'].get_param('algolia_ecommerce.search_key', default='')
        return dict(search_key=search_key)

    def set_admin_key(self):
        self.env['ir.config_parameter'].set_param('algolia_ecommerce.admin_key', (self.admin_key or '').strip())

    def get_default_admin_key(self, fields):
        admin_key = self.env['ir.config_parameter'].get_param('algolia_ecommerce.admin_key', default='')
        return dict(admin_key=admin_key)

    def set_menitor_key(self):
        self.env['ir.config_parameter'].set_param('algolia_ecommerce.menitor_key', (self.menitor_key or '').strip())

    def get_default_menitor_key(self, fields):
        menitor_key = self.env['ir.config_parameter'].get_param('algolia_ecommerce.menitor_key', default='')
        return dict(menitor_key=menitor_key)
