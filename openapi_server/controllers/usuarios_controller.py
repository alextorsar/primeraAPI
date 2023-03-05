import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.usuario import Usuario  # noqa: E501
from openapi_server.models.usuario_reviewer_array import UsuarioReviewerArray  # noqa: E501
from openapi_server import util


def number_reviews_get(limit):  # noqa: E501
    """number_reviews_get

    Obtener los usuarios con un numero de reviews # noqa: E501

    :param limit: numero de reseñas
    :type limit: int

    :rtype: Union[UsuarioReviewerArray, Tuple[UsuarioReviewerArray, int], Tuple[UsuarioReviewerArray, int, Dict[str, str]]
    """
    return 'do some magic!'


def usuario_post(usuario=None):  # noqa: E501
    """usuario_post

    Crear un usuario # noqa: E501

    :param usuario: Introducir datos de usuario
    :type usuario: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        usuario = Usuario.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def usuario_user_id_delete(user_id):  # noqa: E501
    """usuario_user_id_delete

    Eliminar un usuario # noqa: E501

    :param user_id: ID del usuario que quieres eliminar
    :type user_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def usuario_user_id_get(user_id):  # noqa: E501
    """usuario_user_id_get

    Obtener un usuario por su id # noqa: E501

    :param user_id: ID del usuario que quieres devolver
    :type user_id: str

    :rtype: Union[Usuario, Tuple[Usuario, int], Tuple[Usuario, int, Dict[str, str]]
    """
    return 'do some magic!'


def usuario_user_id_put(user_id, usuario=None):  # noqa: E501
    """usuario_user_id_put

    Actualizar información de un usuario # noqa: E501

    :param user_id: ID del usuario que quieres actualizar
    :type user_id: str
    :param usuario: Introducir datos de usuario
    :type usuario: dict | bytes

    :rtype: Union[Usuario, Tuple[Usuario, int], Tuple[Usuario, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        usuario = Usuario.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
