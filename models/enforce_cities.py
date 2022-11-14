from odoo import api, models, fields

# https://www.odoo.com/forum/help-1/replace-city-field-in-res-partner-with-city-id-of-res-city-161839

class ResPartner(models.Model):
    _inherit = 'res.partner'
    city_id = fields.Many2one('res.city', string='City')

    @api.depends('city_id')
    def set_city(self):
       self.city = self.city_id.name
       self.zip = self.city_id.zipcode

    city = fields.Char(compute=set_city, store=True)
