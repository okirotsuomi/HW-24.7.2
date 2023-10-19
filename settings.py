import os

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')

"""Невалидные данные"""
unvalid_email = 'dadon692@songgn.cm'
unvalid_password = '12345'
unvalid_auth_key = {'key': 'b55ed2e13153171d305b49e3cec7dc8dae5b5807c197c40390cce8c7'}