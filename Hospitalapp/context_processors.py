from .models import Package


def menu_links(req):
    
    links=Package.objects.all()
    return dict(links=links)