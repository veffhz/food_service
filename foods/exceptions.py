from rest_framework.exceptions import APIException


class RemoteServiceUnavailable(APIException):
    status_code = 408
    default_detail = 'Сервер недоступен, попробуйте позже'


class HttpBadRequest(APIException):
    status_code = 400
    default_detail = 'Bad Request'
