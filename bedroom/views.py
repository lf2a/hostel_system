# django library
from django.views.generic import ListView, DetailView

# django local
from bedroom.models import Bedroom


class BedroomList(ListView):
    paginate_by = 10
    model = Bedroom

    def get_queryset(self):
        queryset = Bedroom.objects.filter(is_available=True)
        return queryset


class BedroomDetailView(DetailView):
    template_name = 'bedroom/bedroom_detail_view.html'
    model = Bedroom
    context_object_name = 'image'
