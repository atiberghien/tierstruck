from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Tour

class TourDetailView(DetailView):
    model = Tour
    template_name="tour_mgmt/tour.html"
    context_object_name = "tour"

class TourListView(ListView):
    model = Tour
    template_name="tour_mgmt/tours.html"


    def get_context_data(self, **kwargs):
        context = super(TourListView, self).get_context_data()
        context["ongoing_tours"] = context["tour_list"].filter(ongoing=True)
        context["passed_tours"] = context["tour_list"].filter(ongoing=False)
        context["passed_map_settings"] = {
            'DEFAULT_ZOOM' : 5,
            'MIN_ZOOM': 5,
        }
        return context
