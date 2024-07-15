from rest_framework.renderers import JSONRenderer

from .helpers import dict_keys_snake_to_camel


class CamelCaseJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        camelize_data = dict_keys_snake_to_camel(data)
        return super().render(camelize_data, accepted_media_type, renderer_context)