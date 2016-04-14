from django.views import generic

from stream.models import Stream


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'streams'

    def get_queryset(self):
        return Stream.objects.order_by('created_at').all()
