from django.forms import BaseModelForm

from django.http import Http404, HttpResponse, HttpResponseNotFound

from django.shortcuts import render,get_object_or_404

from .models import Category, ShopPost

from django.views.generic import TemplateView, ListView, CreateView, FormView,DetailView

from django.urls import reverse_lazy, reverse

from .forms import ShopPostForm, ContactForm

from  django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.core.mail import EmailMessage

from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin

from django.db import transaction

class CreateShopView(CreateView):
    form_class = ShopPostForm
    template_name = 'buy.html'
    success_url = reverse_lazy('shopapp:index')
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)
    



class IndexView(ListView):
    template_name = 'index.html'
    queryset = ShopPost.objects.order_by('-posted_at')
    paginate_by=9



@login_required
def toggle_bookmark(request, product_id):
    product = get_object_or_404(ShopPost, pk=product_id)
    if product in request.user.bookmarked_products.all():
        # ブックマーク解除
        request.user.bookmarked_products.remove(product)
    else:
        # ブックマーク追加
        request.user.bookmarked_products.add(product)
    return redirect('shopapp:index')  # 適切なリダイレクト先を指定
    
class CategoryView(ListView):
    template_name='index.html'
    paginate_by = 9
    def get_queryset(self):
        category_name = self.kwargs['category']
        try:
            category = Category.objects.filter(title=category_name).get()
        except:
            raise Http404()

        categories = ShopPost.objects.filter(category=category).order_by('-posted_at')
        return categories

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('shopapp:contact')

    def form_valid(self,form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)

        message = \
            '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}' \
            .format(name, email, title, message)
        
        from_email = 'mit2471571@gmail.com'
        to_list = ['mit2471571@gmail.com']
        message = EmailMessage(subject = subject, body = message, from_email = from_email, to = to_list,)
        message.send()
        messages.success(self.request, 'お問い合わせは正常に送信されました。')
        return super().form_valid(form)
        
@method_decorator(login_required, name='dispatch')
class PurchaseConfirmView(TemplateView):
   template_name = 'purchase_confirm.html'
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       ShopPost_id = self.kwargs.get('id')
       stocks = get_object_or_404(ShopPost, id=ShopPost_id)
       context['ShopPost'] = stocks
       return context
   
@method_decorator(login_required, name='dispatch')
class PurchaseView(TemplateView):
   template_name = 'purchase_done.html'
   def post(self, request, *args, **kwargs):
       # 商品の取得
        ShopPost_id = self.kwargs.get('id')
        stocks = get_object_or_404(ShopPost, id=ShopPost_id)
        stocks.delete()

        return render(request, 'purchase_done.html')

@login_required
def bookmark_list(request):
    # 現在ログイン中のユーザーがブックマークした商品を取得
    bookmarked_products = request.user.bookmarked_products.all()
    return render(request, 'bookmarked_list.html', {'bookmarked_items': bookmarked_products})

class MypageView(LoginRequiredMixin,ListView):
    template_name="mypage.html"
    paginate_by = 9
    def get_queryset(self):
        queryset = ShopPost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return queryset
    
class DetailView(DetailView):
    template_name='detail.html'
    model = ShopPost

class UserView(ListView):
    template_name='index.html'
    paginate_by = 9
    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = ShopPost.objects.filter(
            user=user_id).order_by('-posted_at')
        return user_list