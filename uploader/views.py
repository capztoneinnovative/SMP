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




# scheduler_app/views.py

from django.shortcuts import render, redirect
from .forms import ScheduledPostForm, MultipleFileUploadForm
from .models import ScheduledPost
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
        files_form = MultipleFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            scheduled_time = datetime.datetime.combine(post.date, post.time)
            scheduler.add_job(post_to_twitter, 'date', run_date=scheduled_time, args=[post.text, post.image.path if post.image else None])
            return redirect('index')
        if files_form.is_valid():
            for f in request.FILES.getlist('files'):
                handle_uploaded_file(f)
            return redirect('index')
    else:
        form = ScheduledPostForm()
        files_form = MultipleFileUploadForm()
    return render(request, 'index.html', {'form': form, 'files_form': files_form})

def handle_uploaded_file(f):
    with open(f'media/uploads/{f.name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# scheduler_app/views.py

from django.shortcuts import render, redirect
from .forms import ScheduledPostForm, MultipleFileUploadForm
from .models import ScheduledPost
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
        files_form = MultipleFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            scheduled_time = datetime.datetime.combine(post.date, post.time)
            scheduler.add_job(post_to_twitter, 'date', run_date=scheduled_time, args=[post.text, post.image.path if post.image else None])
            return redirect('index')
        if files_form.is_valid():
            for f in request.FILES.getlist('files'):
                handle_uploaded_file(f)
            return redirect('index')
    else:
        form = ScheduledPostForm()
        files_form = MultipleFileUploadForm()
    return render(request, 'index.html', {'form': form, 'files_form': files_form})

def handle_uploaded_file(f):
    with open(f'media/uploads/{f.name}', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# scheduler_app/views.py

from django.shortcuts import render, redirect
from .forms import ScheduledPostForm, MultipleFileUploadForm
from .models import ScheduledPost
from apscheduler.schedulers.background import BackgroundScheduler
import tweepy
import datetime
import os
from django.conf import settings

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
        files_form = MultipleFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            scheduled_time = datetime.datetime.combine(post.date, post.time)
            scheduler.add_job(post_to_twitter, 'date', run_date=scheduled_time, args=[post.text, post.image.path if post.image else None])
            return redirect('index')
        if files_form.is_valid():
            for f in request.FILES.getlist('files'):
                handle_uploaded_file(f)
            return redirect('index')
    else:
        form = ScheduledPostForm()
        files_form = MultipleFileUploadForm()
    return render(request, 'index.html', {'form': form, 'files_form': files_form})

def handle_uploaded_file(f):
    file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', f.name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# scheduler_app/views.py



# scheduler_app/views.py

from django.shortcuts import render, redirect
from .forms import ScheduledPostForm, MultipleFileUploadForm
from .models import ScheduledPost
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import os
from django.conf import settings
import config  # Import the config file

scheduler = BackgroundScheduler()
scheduler.start()

def post_to_social_media(text, image_path=None):
    # Placeholder function for posting to a generic social media API
    if image_path:
        print(f"Posting to social media: {text} with image {image_path}")
    else:
        print(f"Posting to social media: {text}")

def index(request):
    if request.method == 'POST':
        form = ScheduledPostForm(request.POST)
        files_form = MultipleFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            scheduled_time = datetime.datetime.combine(post.date, post.time)
            if files_form.is_valid():
                for f in request.FILES.getlist('files'):
                    handle_uploaded_file(f, post.text, scheduled_time)
            else:
                scheduler.add_job(post_to_social_media, 'date', run_date=scheduled_time, args=[post.text])
            return redirect('index')
    else:
        form = ScheduledPostForm()
        files_form = MultipleFileUploadForm()
    return render(request, 'index.html', {'form': form, 'files_form': files_form})

def handle_uploaded_file(f, text, scheduled_time):
    file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', f.name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    scheduler.add_job(post_to_social_media, 'date', run_date=scheduled_time, args=[text, file_path])



from django.shortcuts import render, redirect
from .forms import MultipleFileUploadForm
from django.conf import settings
import os
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.start()

def post_to_social_media(text, image_path=None):
    # Placeholder function for posting to a generic social media API
    if image_path:
        print(f"Posting to social media: {text} with image {image_path}")
    else:
        print(f"Posting to social media: {text}")

def handle_uploaded_file(f):
    file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', f.name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path

def index(request):
    if request.method == 'POST':
        form = MultipleFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            for f in request.FILES.getlist('files'):
                file_path = handle_uploaded_file(f)
                # Schedule a job or process the file
                post_to_social_media("Scheduled post text", file_path)
            return redirect('index')
    else:
        form = MultipleFileUploadForm()
    return render(request, 'index.html', {'form': form})


# scheduler_app/views.py

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ScheduledPostForm, MultipleFileUploadForm
from django.conf import settings
import os

def index(request):
    if request.method == 'POST':
        if 'files' in request.FILES:
            files_form = MultipleFileUploadForm(request.POST, request.FILES)
            if files_form.is_valid():
                files = request.FILES.getlist('files')
                for f in files:
                    handle_uploaded_file(f)
                return HttpResponseRedirect('/')
        else:
            form = ScheduledPostForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')

    else:
        form = ScheduledPostForm()
        files_form = MultipleFileUploadForm()

    return render(request, 'index.html', {'form': form, 'files_form': files_form})

def handle_uploaded_file(f):
    upload_path = os.path.join(settings.MEDIA_ROOT, 'uploads', f.name)
    with open(upload_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
""" 


from django.shortcuts import render, redirect
from .forms import ScheduledPostForm
from .models import ScheduledPost
from .config import INSTAGRAM_ACCESS_TOKEN, INSTAGRAM_ACCOUNT_ID
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import datetime
import logging

from django.conf import settings

instagram_access_token = settings.INSTAGRAM_ACCESS_TOKEN
instagram_account_id = settings.INSTAGRAM_ACCOUNT_ID

# Configure logging to write to both console and file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('instagram_posting.log'),
        logging.StreamHandler()
    ]
)

scheduler = BackgroundScheduler()
scheduler.start()

def post_to_instagram(text, image_path):
    image_url = f"http://localhost:8000{image_path}"

    # Step 1: Upload the image
    upload_url = f"https://graph.facebook.com/v12.0/{INSTAGRAM_ACCOUNT_ID}/media"
    image_data = {
        'image_url': image_url,
        'caption': text,
        'access_token': INSTAGRAM_ACCESS_TOKEN,
    }
    upload_response = requests.post(upload_url, data=image_data)
    upload_response_data = upload_response.json()
    logging.info("Upload Response: %s", upload_response_data)

    if 'id' in upload_response_data:
        creation_id = upload_response_data['id']
        publish_url = f"https://graph.facebook.com/v12.0/{INSTAGRAM_ACCOUNT_ID}/media_publish"
        publish_data = {
            'creation_id': creation_id,
            'access_token': INSTAGRAM_ACCESS_TOKEN,
        }
        publish_response = requests.post(publish_url, data=publish_data)
        logging.info("Publish Response: %s", publish_response.json())
        return publish_response.json()
    else:
        logging.error("Error uploading image: %s", upload_response_data)
        return upload_response_data

def index(request):
    if request.method == 'POST':
        form = ScheduledPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            scheduled_time = datetime.datetime.combine(post.date, post.time)
            scheduler.add_job(
                post_to_instagram, 
                'date', 
                run_date=scheduled_time, 
                args=[post.text, post.image.url],
                misfire_grace_time=3600  # 1 hour grace period
            )
            return redirect('index')
    else:
        form = ScheduledPostForm()
    return render(request, 'index.html', {'form': form})

