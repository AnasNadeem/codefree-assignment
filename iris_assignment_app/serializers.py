from rest_framework.serializers import ModelSerializer
from iris_assignment_app.models import Iris

class IrisSerializer(ModelSerializer):
    class Meta:
        model = Iris
        fields = "__all__"
