# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import json

from algoliasearch import algoliasearch
from odoo import http
from odoo.addons.website.controllers.main import Website
from odoo.http import request


class Website(Website):

    # overriding the methods used by website_field_autocomplete
    @http.route(
        '/website/field_autocomplete/<string:model>',
        type='http',
        auth='public',
        methods=['GET'],
        website=True,
    )
    def _get_field_autocomplete(self, model, **kwargs):
        """ Return json autocomplete data """
        domain = json.loads(kwargs.get('domain', "[]"))
        fields = json.loads(kwargs.get('fields', "[]"))
        limit = kwargs.get('limit', None)
        res = self._get_autocomplete_data(model, domain, fields, limit)
        return json.dumps(res.values())

    def _get_autocomplete_data(self, model, domain, fields, limit=None):
        #
        """ Gets and returns raw record data
        Params:
            model: Model name to query on
            domain: Search domain
            fields: List of fields to get
            limit: Limit results to
        Returns:
            Dict of record dicts, keyed by ID
        """
        # if model is product we will search our database and algolia index and compine the results
        if (model == 'product.product'):

            params = request.env['ir.config_parameter'].sudo()
            application_id = params.get_param('algolia_ecommerce.application_id', default='')
            admin_key = params.get_param('algolia_ecommerce.admin_key', default='')

            client = algoliasearch.Client(application_id, admin_key)
            index = client.init_index('products')
            ids = []
            # get the data from algolia
            algolia = index.search(domain[-1][-1])
            for a in algolia['hits']:
                ids.append(int(a['objectID']))
            if limit:
                limit = int(limit)
            res = request.env[model].search_read(
                domain, fields, limit=limit
            )
            for r in res:
                if r['id'] in ids:
                    ids.remove(r['id'])
            if len(ids) > 0:
                res2 = request.env[model].search_read([('id', 'in', ids)], fields, limit=limit)
                res = res + res2
            oo = {r['id']: r for r in res}
            return oo
        else:
            if limit:
                limit = int(limit)
            res = request.env[model].search_read(
                domain, fields, limit=limit
            )
            return {r['id']: r for r in res}
