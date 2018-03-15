# # -*- coding: utf-8 -*-
#
#
from algoliasearch import algoliasearch
from odoo import models, api


#
#
# class algolia_ecommerce(models.Model):
#     _name = 'algolia_ecommerce.config.api'
#
#     application_id = fields.Char('Application ID', require=True)
#     search_key = fields.Char('Search Only API Key', require=True)
#     admin_key = fields.Char('Admin API Key')
#     menitor_key = fields.Char('Monitoring API Key')
#
#     @api.model
#     def does(self):
#         client = algoliasearch.Client("KWVGPGG31L", 'ef1a2a2ed71b0bcd84cf38682741156a')
#         index = client.init_index('your_index_name')
#
#         index = client.init_index("contact")
#         batch = json.load(open('contacts.json'))
#         index.add_objects(batch)
#         index.set_settings({"searchableAttributes": ["lastname", "firstname", "company",
#                                                      "email", "city", "address"]})
#
#
# class algolia_index(models.Model):
#     _name = 'algolia_ecommerce.index'
#
#     index_name = fields.Char('Index Name')
#     algolia_config = fields.Many2one('algolia_ecommerce.config.api', string='Algolia Config')
#     model = fields.Many2one('ir.model', 'Corresponding Model')
#
#     @api.multi
#     def get_index(self):
#         for rec in self:
#             client = algoliasearch.Client(rec.algolia_config.application_id, rec.algolia_config.admin_key, )
#             if rec.index_name is not None and len(rec.index_name) > 0:
#                 index = client.init_index(rec.index_name)
#             else:
#                 index = client.init_index(str(rec.model.model))
#
#             return index
#
#
class ProductProduct(models.Model):
    _inherit = "product.product"

    # override create function
    @api.model
    def create(self, vals):
        res = super(ProductProduct, self).create(vals)
        # add object to the index
        params = self.env['ir.config_parameter'].sudo()
        application_id = params.get_param('algolia_ecommerce.application_id', default='')
        admin_key = params.get_param('algolia_ecommerce.admin_key', default='')

        client = algoliasearch.Client(application_id, admin_key)
        index = client.init_index('products')

        res_al = index.add_object(
            {"name": res.product_tmpl_id.name, "description": res.product_tmpl_id.description,
             'barcode': res.barcode, "objectID": res.id})
        return res

    @api.multi
    def write(self, vals):
        res = super(ProductProduct, self).write(vals)
        # update the object in the index
        params = self.env['ir.config_parameter'].sudo()

        application_id = params.get_param('algolia_ecommerce.application_id', default='')
        admin_key = params.get_param('algolia_ecommerce.admin_key', default='')

        client = algoliasearch.Client(application_id, admin_key)
        index = client.init_index('products')
        # print('asdasd',index)
        index.save_object(
            {"name": self.product_tmpl_id.name, "description": self.product_tmpl_id.description,
             'barcode': self.barcode, "objectID": self.id})
        return res
    #TODO override the unlink function
    #TODO override the copy function