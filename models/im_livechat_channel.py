# -*- coding: utf-8 -*-

from odoo import fields, models

class LiveChat(models.Model):
	_inherit = 'im_livechat.channel'
	
	name = fields.Char(translate=True)
	button_text	 = fields.Char(translate=True)
	input_placeholder = fields.Char(translate=True)
	default_message = fields.Char(translate=True)
