from rest_framework.viewsets import ModelViewSet
from .models import Project, Measurement
from .serializers import ProjectModelSerializer, MeasurementModelSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    """ViewSet для проекта."""
    # TODO: добавьте конфигурацию для объекта


class MeasurementViewSet(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementModelSerializer
    """ViewSet для измерения."""
    # TODO: добавьте конфигурацию для измерения
