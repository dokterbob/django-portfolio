from .models import Collection, Artwork


def collections(request):
    """ Add `collections` to RequestContext. """

    return {'collections': Collection.objects.all()}


def artworks(request):
    """ Add `artworks` to RequestContext. """

    return {'artworks': Artwork.objects.all()}
