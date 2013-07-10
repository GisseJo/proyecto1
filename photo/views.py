from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.forms import ModelForm
from proyecto1.settings import MEDIA_URL, STATIC_URL

from photo.models import *

def main(request):
    """Main listing."""
    albums = Album.objects.all()
    if not request.user.is_authenticated():
        albums = albums.filter(public=True)

    paginator = Paginator(albums, 10)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        albums = paginator.page(page)
    except (InvalidPage, EmptyPage):
        albums = paginator.page(paginator.num_pages)

    for album in albums.object_list:
        album.images = album.image_set.all()[:4]

    return render_to_response("photo/list.html", dict(albums=albums, user=request.user,
        media_url=MEDIA_URL, static_url=STATIC_URL))

@login_required
def search(request):
    """Search, filter, sort images."""
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    p = request.POST
    images = defaultdict(dict)

    # init parameters
    parameters = {}
    keys = ("title filename rating_from rating_to width_from width_to height_from height_to tags view"
        " user sort asc_desc").split()
    for k in keys:
        parameters[k] = ''
    parameters["album"] = []

    # create dictionary of properties for each image and a dict of search/filter parameters
    for k, v in p.items():
        if k == "album":
            parameters[k] = [int(x) for x in p.getlist(k)]
        elif k == "user":
            if v != "all": v = int(v)
            parameters[k] = v
        elif k in parameters:
            parameters[k] = v
        elif k.startswith("title") or k.startswith("rating") or k.startswith("tags"):
            k, pk = k.split('-')
            images[pk][k] = v
        elif k.startswith("album"):
            pk = k.split('-')[1]
            images[pk]["albums"] = p.getlist(k)

    # save or restore parameters from session
    if page != 1 and "parameters" in request.session:
        parameters = request.session["parameters"]
    else:
        request.session["parameters"] = parameters

    results = update_and_filter(request, images, parameters)

    # make paginator
    paginator = Paginator(results, 20)
    try:
        results = paginator.page(page)
    except (InvalidPage, EmptyPage):
        request = paginator.page(paginator.num_pages)

    # add list of tags as string and list of album names to each image object
    for img in results.object_list:
        tags = [x[1] for x in img.tags.values_list()]
        img.tag_lst = join(tags, ', ')
        img.album_lst = [x[1] for x in img.albums.values_list()]

    d = dict(results=results, user=request.user, albums=Album.objects.all(), prm=parameters,
             users=User.objects.all(), media_url=MEDIA_URL)
    d.update(csrf(request))
    return render_to_response("photo/search.html", d)

def album(request, pk):
    """Album listing."""
    album = Album.objects.get(pk=pk)
    if not album.public and not request.user.is_authenticated():
        return HttpResponse("Error: you need to be logged in to view this album.")

    images = album.image_set.all()
    paginator = Paginator(images, 30)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        images = paginator.page(page)
    except (InvalidPage, EmptyPage):
        images = paginator.page(paginator.num_pages)

    return render_to_response("photo/album.html", dict(album=album, images=images, user=request.user,
        media_url=MEDIA_URL))

def image(request, pk):
    """Image page."""
    img = Image.objects.get(pk=pk)
    return render_to_response("photo/image.html", dict(image=img, user=request.user,
         backurl=request.META["HTTP_REFERER"], media_url=MEDIA_URL))