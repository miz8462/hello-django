from django.http import HttpResponse
from django.views.generic import TemplateView


def helloworldfunction(request):
    returned_object = HttpResponse('doskoi')
    return returned_object


class HelloWorldClass(TemplateView):
    template_name = 'hello.html'
