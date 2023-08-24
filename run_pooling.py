import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flowershop.settings')
django.setup()


from flowershop_bot.dispatcher import run_pooling


if __name__ == "__main__":
    run_pooling()
