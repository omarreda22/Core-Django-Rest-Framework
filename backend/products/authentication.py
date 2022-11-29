from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


# over wtire
class TokenAuthentication(BaseTokenAuth):
    keyword = 'CustomKeyword'
