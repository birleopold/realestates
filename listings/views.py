from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, district_choices

from .models import Listing, Land

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)
  
  paginator = Paginator(listings, 6)
  
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)
  

  context = {
    'listings': paged_listings,
    
  }
  return render(request, 'listings/listings.html', context)

  
def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
  context = {
    'listing': listing
  }
  return render(request, 'listings/listing.html', context)

def lands(request):
  lands = Land.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(lands, 6)

  page = request.GET.get('page')
  paged_lands = paginator.get_page(page)

  context = {
      'lands': paged_lands,
  }
  return render(request, 'land/lands.html', context)


def land(request, plot_id):
  land = get_object_or_404(Land, pk=plot_id)
  context = {
      'land': land
  }

  return render(request, 'land/land.html', context)


def search(request):
  queryset_list = Listing.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # district
  if 'district' in request.GET:
    district = request.GET['district']
    if district:
      queryset_list = queryset_list.filter(district__iexact=district)

  # town
  if 'town' in request.GET:
    town = request.GET['town']
    if state:
      queryset_list = queryset_list.filter(state__iexact=town)

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
    'district_choices': district_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context)
