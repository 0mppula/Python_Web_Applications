from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """ The homepage for learning Log.  """
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """ Displays all topics. """

    if request.user.is_superuser:
        topics = Topic.objects.all().order_by('date_added')
    else:
        owned_topics = Topic.objects.filter(owner=request.user)
        public_topics = Topic.objects.filter(public=True)
        topics = owned_topics.union(public_topics).order_by('date_added')
        
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """ Display a single topic and all its entries. """
    topic = get_object_or_404(Topic, id=topic_id)

    # Confirm topic ownership before displaying
    if check_user_rights(request, topic.owner):
        entries = topic.entry_set.order_by('-date_added')
        context = {'topic': topic, 'entries': entries}
        return render(request, 'learning_logs/topic.html', context)
    else:
        raise Http404


@login_required
def new_topic(request):
    """ Add a new topic. """
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TopicForm()
    else:
        # POST data submitted; process data
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """ Add a new entry to a topic. """
    topic = get_object_or_404(Topic, id=topic_id)

    if check_user_rights(request, topic.owner):
        if request.method != 'POST':
            # No data submitted create a blank form
            form = EntryForm()
        else:
            # POST data submitted; process data
            form = EntryForm(request.POST)
            if form.is_valid():
                new_entry = form.save(commit=False)
                new_entry.topic = topic
                form.save()
                return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    
        context = {'topic': topic, 'form': form}
        return render(request, 'learning_logs/new_entry.html', context)
    else:
        raise Http404


@login_required
def edit_entry(request, entry_id):
    """ Edit an existing topic. """
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic

    # If user tries to add entry to other users logs
    if check_user_rights(request, topic.owner):
        pass
    else:
        return HttpResponseRedirect(reverse('learning_logs:topics'))

    if request.method != 'POST':
        # Initial request; pre-fill form with current entry
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

def check_user_rights(request, owner):
    """ Check if user owns a topic or is a super user. """
    if request.user == owner:
        return True
    elif request.user.is_superuser:
        return True
    else:
        return False