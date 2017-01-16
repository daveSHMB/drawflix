from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime, timedelta
from drawflix.models import Drawing
from drawflix.forms import DrawingForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    context_dict = {}
    visits = request.session.get('visits')
    if not visits:
        visits = 1
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        if (datetime.now() - last_visit_time).seconds > 0:
            # ...reassign the value of the cookie to +1 of what it was before...
            visits = visits + 1
            # ...and update the last visit cookie, too.
            reset_last_visit_time = True
    else:
        # Cookie last_visit doesn't exist, so create it to the current date/time.
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits
    context_dict['visits'] = visits

    form = DrawingForm()
    context_dict['form'] = form
    response = render(request,'drawflix/index.html', context_dict)

    return response


def about(request):
    return render(request, 'drawflix/about.html')


def most_recent(request):
    recent_drawings = Drawing.objects.order_by('-date')[:15]
    context_dict = {'recent_drawings': recent_drawings}
    return render(request, 'drawflix/most_recent.html', context_dict)


def trending(request):
    end_date = datetime.now()
    start_date = end_date - timedelta(days = 7)
    trending_drawings = Drawing.objects.filter(date__range=[start_date, end_date]).order_by('-likes')[:25]
    context_dict = {'trending_drawings': trending_drawings}
    return render(request, 'drawflix/trending.html', context_dict)

def hall_of_fame(request):
    hall_of_fame = Drawing.objects.order_by('-likes')[:15]
    context_dict = {'hall_of_fame': hall_of_fame}
    return render(request, 'drawflix/hall_of_fame.html', context_dict)

def user_drawings(request):
    user_drawings = Drawing.objects.filter(user=request.user)
    context_dict = {'user_drawings': user_drawings}
    return render(request, 'drawflix/user_drawings.html', context_dict)

def archive(request):
    drawing_list = Drawing.objects.all()
    paginator = Paginator(drawing_list, 12) # Show 10 drawings per page

    page = request.GET.get('page')
    try:
        drawings = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        drawings = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    context_dict = {'drawings': drawings}

    return render(request, 'drawflix/archive.html', context_dict)


def add_drawing(request):

    if request.method == 'POST':
        form = DrawingForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            drawing = form.save(commit=False)
            if request.user.is_authenticated():
                drawing.user = request.user
            drawing.save()
        else:
            # The supplied form contained errors
            print form.errors

    return most_recent(request)


@login_required # user must be logged in to like drawings
def like_drawing(request):

    drawing_id = None
    if request.method == 'GET':
        drawing_id = request.GET['drawing_id']

    likes = 0
    if drawing_id:
        drawing = Drawing.objects.get(id=int(drawing_id))
        if drawing:
            likes = drawing.likes + 1
            drawing.likes = likes
            drawing.save()

    return HttpResponse(likes)
