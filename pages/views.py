from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Article, Categorie
from django.shortcuts import render
from .models import MessageContact






def home(request):
    latest_articles = Article.objects.order_by('-date_pub')[:3]
    return render(request, 'pages/home.html', {'latest_articles': latest_articles})

def blog(request):
    query = request.GET.get('q', '')
    categorie_id = request.GET.get('categorie', '')
    article_list = Article.objects.all()

    # Recherche dans titre et contenu (insensible à la casse)
    if query:
        article_list = article_list.filter(
            Q(titre__icontains=query) | Q(contenu__icontains=query)
        )
    # Filtre catégorie si défini
    if categorie_id:
        article_list = article_list.filter(categorie__id=categorie_id)

    article_list = article_list.order_by('-date_pub')

    paginator = Paginator(article_list, 6)  # 6 articles par page
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)

    categories = Categorie.objects.all()

    context = {
        'articles': articles,
        'categories': categories,
        'query': query,
        'categorie_id': categorie_id,
    }
    return render(request, 'pages/blog.html', context)

def article_detail(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    article.nombre_vues +=1
    article.save()

    return render(request, 'pages/article_detail.html', {'article': article})


def contact(request):
    success = False
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')

        # Sauvegarde dans la base
        MessageContact.objects.create(
            nom=nom,
            email=email,
            sujet=sujet,
            message=message
        )

        success = True

    return render(request, 'pages/contact.html', {'success': success})




def about(request):
    return render(request, 'pages/about.html')


from django.shortcuts import render, get_object_or_404
from .models import Service, Article
from pages.models import Categorie,Service,ImageService,Article
def services_list(request):
    services = Service.objects.all()
    return render(request, 'pages/services_list.html', {'services': services})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    articles = Article.objects.filter(categorie=service.categorie).order_by('-date_pub')[:3]  # 3 articles récents
    return render(request, 'pages/service_detail.html', {
        'service': service,
        'articles': articles,
    })

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
def contact(request):
    if request.method == 'POST':
        try:
            # Récupération des données
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            # Envoi d'email
            send_mail(
                subject=f"[Contact] {subject}",
                message=f"Message de {name} ({email}):\n\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            # Confirmation
            messages.success(request, "Votre message a été envoyé avec succès !")
            return HttpResponseRedirect(request.path)
       
        except Exception as e:
            messages.error(request, f"Erreur lors de l'envoi: {str(e)}")
   
    return render(request, 'pages/contact.html')