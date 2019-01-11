from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.utils import ErrorList
from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from .models import Tweet
from .mixins import FormUserNeededMixin,UserOwnerMixin
from .forms import TweetModelForm
from django.views.generic import (DetailView,
                                ListView, 
                                CreateView,
                                UpdateView,
                                DeleteView)

# Create your views here.
class TweetCreateView(FormUserNeededMixin,CreateView):
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    # fields = ['user', 'content'] 
    # success_url = "/tweet/create/"
    # login_url = '/admin/'

    # def form_valid(self, form):
    #     if self.request.user.is_authenticated():
    #         form.instance.user = self.request.user
    #         return super(TweetCreateView, self).form_valid(form)
    #     else:
    #         form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList([" User must be logged in  to continue "])
    #         return self.form_invalid(form)    



class TweetDetailView(DetailView):
    template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()

    # def get_object(self):
    #     print(self.kwargs)
    #     pk = self.kwargs.get("pk")
    #     obj = get_object_or_404(Tweet,pk)
    #     return Tweet.objects.get(id=pk )

class TweetListView(LoginRequiredMixin,ListView):
    template_name = "tweets/list_view.html"
    queryset = Tweet.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user_id__username__icontains=query)
                    )
        return qs
    

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)

        # context["another_list"] = Tweet.objects.all()
        # print(context)
        return context

class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin,UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = "/tweet/"


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy("tweet:list") #reverse()    



# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id)
#     context = {
#         "object":obj
#     }
#     return render(request,"tweets/detail_view.html", context)

# def tweet_list_view(request, id=1):
#     queryset = Tweet.objects.all()
#     context = {
#         "object_list":queryset
#     }
#     return render(request,"tweets/list_view.html",context)    