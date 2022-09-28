# Part of OpenSPP. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class OpenSPPRegistrant(models.Model):
    _name = "res.partner"
    _inherit = [_name, "base_multi_image.owner"]

    image_ids = fields.One2many(comodel_name="base_multi_image.image")
