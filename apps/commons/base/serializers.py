from rest_framework import serializers

from apps.commons.exceptions import InvalidParameterFormatException
from apps.commons.utils import inline_serializer


class BaseSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "data" in kwargs and not self.is_valid():
            raise InvalidParameterFormatException(self.errors)

    class Meta:
        ref_name = None


class BaseResponseSerializer(serializers.Serializer):
    code = serializers.CharField(default="request_success")
    success = serializers.BooleanField(default=True)
    message = serializers.CharField(default="Request was successful.")

    def __init__(self, *args, **kwargs):
        data_serializer = kwargs.pop("data_serializer", None)
        pagination_serializer = kwargs.pop("pagination_serializer", False)
        self.data_serializer_many = kwargs.pop("data_serializer_many", False)
        super().__init__(*args, **kwargs)

        if data_serializer is not None and pagination_serializer is False:
            self.fields["data"] = self.get_data_field(data_serializer)

        elif data_serializer is not None and pagination_serializer is True:
            self.fields["data"] = self.get_pagination_field(data_serializer)

    def get_data_field(self, data_serializer):
        data_field = data_serializer()

        if self.data_serializer_many is True:
            return serializers.ListSerializer(child=data_field, allow_empty=False)
        else:
            return data_field

    def get_pagination_field(self, data_serializer):
        return inline_serializer(
            fields={
                "limit": serializers.IntegerField(default=15),
                "offset": serializers.IntegerField(default=0),
                "count": serializers.IntegerField(default=0),
                "next": serializers.URLField(),
                "previous": serializers.URLField(),
                "results": serializers.ListSerializer(child=data_serializer(), allow_empty=False),
            },
        )

    class Meta:
        ref_name = None
