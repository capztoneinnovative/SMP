"""
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


from django.shortcuts import render, redirect
from .forms import ScheduledPostForm
from apscheduler.schedulers.background import BackgroundScheduler
import datetime

scheduler = BackgroundScheduler()
scheduler.start()

def post_to_social_media(text, image_path):
    # Placeholder function to post to social media
    print(f"Posting to social media: Text: {text}, Image Path: {image_path}")

def index(request):
    if request.method == 'POST':
        form = ScheduledPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            scheduled_time = datetime.datetime.combine(post.date, post.time)
            scheduler.add_job(post_to_social_media, 'date', run_date=scheduled_time, args=[post.text, post.image.path if post.image else None])
            return redirect('index')
    else:
        form = ScheduledPostForm()
    return render(request, 'index.html', {'form': form})
""" 

# scheduler_app/views.py

from django.shortcuts import render, redirect
from .forms import ScheduledPostForm
from apscheduler.schedulers.background import BackgroundScheduler
import tweepy
import datetime

# Twitter API credentials
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

scheduler = BackgroundScheduler()
scheduler.start()

def post_to_twitter(text, image_path):
    if image_path:
        api.update_status_with_media(status=text, filename=image_path)
    else:
        api.update_status(status=text)

def index(request):
    if request.method == 'POST':
        form = ScheduledPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            scheduled_time = datetime.datetime.combine(post.date, post.time)
            scheduler.add_job(post_to_twitter, 'date', run_date=scheduled_time, args=[post.text, post.image.path if post.image else None])
            return redirect('index')
    else:
        form = ScheduledPostForm()
    return render(request, 'index.html', {'form': form})
