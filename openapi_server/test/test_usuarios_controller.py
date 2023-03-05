# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.usuario import Usuario  # noqa: E501
from openapi_server.models.usuario_reviewer_array import UsuarioReviewerArray  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUsuariosController(BaseTestCase):
    """UsuariosController integration test stubs"""

    def test_number_reviews_get(self):
        """Test case for number_reviews_get

        
        """
        query_string = [('limit', 56)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/usuario',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuario_post(self):
        """Test case for usuario_post

        
        """
        usuario = {"correo":"correo","direccion":"direccion","userId":0,"nombre":"nombre"}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/usuario',
            method='POST',
            headers=headers,
            data=json.dumps(usuario),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuario_user_id_delete(self):
        """Test case for usuario_user_id_delete

        
        """
        query_string = [('userId', 'user_id_example')]
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/usuario/',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuario_user_id_get(self):
        """Test case for usuario_user_id_get

        
        """
        query_string = [('userId', 'user_id_example')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/usuario/',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usuario_user_id_put(self):
        """Test case for usuario_user_id_put

        
        """
        usuario = {"correo":"correo","direccion":"direccion","userId":0,"nombre":"nombre"}
        query_string = [('userId', 'user_id_example')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/usuario/',
            method='PUT',
            headers=headers,
            data=json.dumps(usuario),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
