from rest_framework import viewsets


class BaseViewSet(viewsets.ModelViewSet):
    lookup_field = 'uuid'
