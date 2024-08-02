"""
# scheduler_app/management/commands/start_monitor.py

from django.core.management.base import BaseCommand
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from django.conf import settings
import os
import time
import tweepy

# Twitter API credentials
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

class Command(BaseCommand):
    help = 'Starts monitoring the media directory for new files'

    def handle(self, *args, **kwargs):
        media_directory = os.path.join(settings.MEDIA_ROOT, 'uploads')
        event_handler = FileEventHandler()
        observer = Observer()
        observer.schedule(event_handler, media_directory, recursive=False)
        observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

class FileEventHandler(FileSystemEventHandler):
    def process(self, event):
        if event.event_type == 'created':
            # New file detected
            self.handle_new_file(event.src_path)

    def handle_new_file(self, file_path):
        if file_path.endswith(('.png', '.jpg', '.jpeg')):
            self.upload_image(file_path)
        elif file_path.endswith('.txt'):
            self.upload_text(file_path)

    def upload_image(self, file_path):
        api = self.get_twitter_api()
        api.update_status_with_media(status="Automated post with image", filename=file_path)

    def upload_text(self, file_path):
        api = self.get_twitter_api()
        with open(file_path, 'r') as file:
            text = file.read()
            api.update_status(status=text)

    def get_twitter_api(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return tweepy.API(auth)


# scheduler_app/management/commands/start_monitor.py

import os
import time
import tweepy
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from django.core.management.base import BaseCommand

# Twitter API credentials
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            if file_path.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                self.upload_image(file_path)
            elif file_path.endswith('.txt'):
                self.upload_text(file_path)

    def upload_image(self, file_path):
        api = self.get_twitter_api()
        api.update_status_with_media(status="Automated post with image", filename=file_path)

    def upload_text(self, file_path):
        api = self.get_twitter_api()
        with open(file_path, 'r') as file:
            text = file.read()
            api.update_status(status=text)

    def get_twitter_api(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return tweepy.API(auth)

class Command(BaseCommand):
    help = 'Starts the file monitor for the media directory'

    def handle(self, *args, **kwargs):
        media_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../media/uploads')
        event_handler = FileEventHandler()
        observer = Observer()
        observer.schedule(event_handler, media_directory, recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
  
# scheduler_app/management/commands/start_monitor.py

import os
import time
import tweepy
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from django.core.management.base import BaseCommand

# Twitter API credentials
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            if file_path.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                self.upload_image(file_path)
            elif file_path.endswith('.txt'):
                self.upload_text(file_path)

    def upload_image(self, file_path):
        api = self.get_twitter_api()
        api.update_status_with_media(status="Automated post with image", filename=file_path)

    def upload_text(self, file_path):
        api = self.get_twitter_api()
        with open(file_path, 'r') as file:
            text = file.read()
            api.update_status(status=text)

    def get_twitter_api(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return tweepy.API(auth)

class Command(BaseCommand):
    help = 'Starts the file monitor for the media directory'

    def handle(self, *args, **kwargs):
        media_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../media/uploads')
        event_handler = FileEventHandler()
        observer = Observer()
        observer.schedule(event_handler, media_directory, recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()


# scheduler_app/management/commands/start_monitor.py

import os
import time
import tweepy
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from django.core.management.base import BaseCommand
from django.conf import settings

# Twitter API credentials
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            if file_path.endswith(('.png', '.jpg', '.jpeg', '.gif', '.txt')):
                self.handle_file(file_path)

    def handle_file(self, file_path):
        if file_path.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            self.upload_image(file_path)
        elif file_path.endswith('.txt'):
            self.upload_text(file_path)
        self.move_file_to_deleted(file_path)

    def upload_image(self, file_path):
        api = self.get_twitter_api()
        api.update_status_with_media(status="Automated post with image", filename=file_path)

    def upload_text(self, file_path):
        api = self.get_twitter_api()
        with open(file_path, 'r') as file:
            text = file.read()
            api.update_status(status=text)

    def get_twitter_api(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return tweepy.API(auth)

    def move_file_to_deleted(self, file_path):
        deleted_folder = os.path.join(settings.MEDIA_ROOT, 'deleted')
        if not os.path.exists(deleted_folder):
            os.makedirs(deleted_folder)
        new_path = os.path.join(deleted_folder, os.path.basename(file_path))
        os.rename(file_path, new_path)

class Command(BaseCommand):
    help = 'Starts the file monitor for the media directory'

    def handle(self, *args, **kwargs):
        media_directory = os.path.join(settings.MEDIA_ROOT, 'uploads')
        event_handler = FileEventHandler()
        observer = Observer()
        observer.schedule(event_handler, media_directory, recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()


# scheduler_app/management/commands/start_monitor.py

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from django.core.management.base import BaseCommand
from django.conf import settings
import SMP.config as config  # Import the config file

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            if file_path.endswith(('.png', '.jpg', '.jpeg', '.gif', '.txt')):
                self.handle_file(file_path)

    def handle_file(self, file_path):
        if file_path.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            self.upload_image(file_path)
        elif file_path.endswith('.txt'):
            self.upload_text(file_path)
        self.move_file_to_deleted(file_path)

    def upload_image(self, file_path):
        print(f"Uploading image to social media: {file_path}")

    def upload_text(self, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
            print(f"Uploading text to social media: {text}")

    def move_file_to_deleted(self, file_path):
        deleted_folder = os.path.join(settings.MEDIA_ROOT, 'deleted')
        if not os.path.exists(deleted_folder):
            os.makedirs(deleted_folder)
        new_path = os.path.join(deleted_folder, os.path.basename(file_path))
        os.rename(file_path, new_path)

class Command(BaseCommand):
    help = 'Starts the file monitor for the media directory'

    def handle(self, *args, **kwargs):
        media_directory = os.path.join(settings.MEDIA_ROOT, 'uploads')
        event_handler = FileEventHandler()
        observer = Observer()
        observer.schedule(event_handler, media_directory, recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
 

# scheduler_app/management/commands/start_monitor.py

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from django.core.management.base import BaseCommand
from django.conf import settings
import config  # Import the config file

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            if file_path.endswith(('.png', '.jpg', '.jpeg', '.gif', '.txt')):
                self.handle_file(file_path)

    def handle_file(self, file_path):
        if file_path.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            self.upload_image(file_path)
        elif file_path.endswith('.txt'):
            self.upload_text(file_path)
        self.move_file_to_deleted(file_path)

    def upload_image(self, file_path):
        print(f"Uploading image to social media: {file_path}")

    def upload_text(self, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
            print(f"Uploading text to social media: {text}")

    def move_file_to_deleted(self, file_path):
        deleted_folder = os.path.join(settings.MEDIA_ROOT, 'deleted')
        if not os.path.exists(deleted_folder):
            os.makedirs(deleted_folder)
        new_path = os.path.join(deleted_folder, os.path.basename(file_path))
        os.rename(file_path, new_path)

class Command(BaseCommand):
    help = 'Starts the file monitor for the media directory'

    def handle(self, *args, **kwargs):
        media_directory = os.path.join(settings.MEDIA_ROOT, 'uploads')
        event_handler = FileEventHandler()
        observer = Observer()
        observer.schedule(event_handler, media_directory, recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()


# scheduler_app/management/commands/start_monitor.py

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from django.core.management.base import BaseCommand
from django.conf import settings
import config  # Import the config file

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            if file_path.endswith(('.png', '.jpg', '.jpeg', '.gif', '.txt')):
                self.handle_file(file_path)

    def handle_file(self, file_path):
        if file_path.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            self.upload_image(file_path)
        elif file_path.endswith('.txt'):
            self.upload_text(file_path)
        self.move_file_to_deleted(file_path)

    def upload_image(self, file_path):
        print(f"Uploading image to social media: {file_path}")

    def upload_text(self, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
            print(f"Uploading text to social media: {text}")

    def move_file_to_deleted(self, file_path):
        deleted_folder = os.path.join(settings.MEDIA_ROOT, 'deleted')
        if not os.path.exists(deleted_folder):
            os.makedirs(deleted_folder)
        new_path = os.path.join(deleted_folder, os.path.basename(file_path))
        os.rename(file_path, new_path)

class Command(BaseCommand):
    help = 'Starts the file monitor for the media directory'

    def handle(self, *args, **kwargs):
        media_directory = os.path.join(settings.MEDIA_ROOT, 'uploads')
        event_handler = FileEventHandler()
        observer = Observer()
        observer.schedule(event_handler, media_directory, recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
""" 

# scheduler_app/management/commands/start_monitor.py
# scheduler_app/management/commands/start_monitor.py

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from django.core.management.base import BaseCommand
from django.conf import settings

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            if file_path.endswith(('.png', '.jpg', '.jpeg', '.gif', '.txt')):
                self.handle_file(file_path)

    def handle_file(self, file_path):
        if file_path.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            self.upload_image(file_path)
        elif file_path.endswith('.txt'):
            self.upload_text(file_path)
        self.move_file_to_deleted(file_path)

    def upload_image(self, file_path):
        print(f"Uploading image to social media: {file_path}")

    def upload_text(self, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
            print(f"Uploading text to social media: {text}")

    def move_file_to_deleted(self, file_path):
        deleted_folder = os.path.join(settings.MEDIA_ROOT, 'deleted')
        if not os.path.exists(deleted_folder):
            os.makedirs(deleted_folder)
        new_path = os.path.join(deleted_folder, os.path.basename(file_path))
        os.rename(file_path, new_path)

class Command(BaseCommand):
    help = 'Starts the file monitor for the media directory'

    def handle(self, *args, **kwargs):
        media_directory = os.path.join(settings.MEDIA_ROOT, 'uploads')
        event_handler = FileEventHandler()
        observer = Observer()
        observer.schedule(event_handler, media_directory, recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

