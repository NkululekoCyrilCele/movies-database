from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, Http404

from .models import MovieList


def index(request):
    movies = MovieList.objects.all()
    # output = ', '.join([movie.title for movie in movies])
    # return HttpResponse(output)
    return render(request, 'movies/index.html', {
        'movies': movies
    })


# def details(request, pk):
#    try:
#        movie = MovieList.objects.get(id=pk)
#        return render(request, 'movies/details.html', {
#            'movie': movie
#        })
#    except MovieList.DoesNotExist:
#        raise Http404()

def details(request, pk):
    movie = get_object_or_404(MovieList, id=pk)
    return render(request, 'movies/details.html', {
        'movie': movie
    })
