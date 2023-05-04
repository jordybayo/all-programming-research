from django.shortcuts import render, get_object_or_404


from .models import Album,Artists,Contact,Booking 

# Create your views here.
def index(request):
	albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
	formated_albums = ["<li>{}</li>".format(album.title) for album in albums]
	context = {'albums' : albums}
	return render(request, 'store/index.html', context)

def listing(request):
	albums = Album.objects.filter(available=True)
	context = {
		'albums': albums
	}
	return render(request, 'store/listing.html', context)

def detail(request, album_id):
	albums = get_object_or_404(Album, pk=album_id)
	artists = " ".join([artist.name for artist in Artists.objects.all()])
	context = {
		'album_title'	:	albums.title,
		'album_id'		:	albums.id,
		'thumbnail'		:	albums.picture,
	}
	return render(request, 'store/detail.html', context)


def search(request):
	query = request.GET.get('query')  
	if not query:
		message = Album.objects.all()
	else:

		albums = Album.objects.filter(title__icontains=query)

	if not albums.exists():
		albums = Album.objects.filter(artists__name__icontains=query)

	title = "Resultat de la recherche %s"%query
	context = {
		'albums': albums, 
		'title': title
	}
	return render(request, 'store/search.html', context)
