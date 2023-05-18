from celery import shared_task

from news_list.models import News


# @shared_task
# def send_email_news()