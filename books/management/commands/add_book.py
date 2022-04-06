
from books.models import Book
from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):

     def handle(self, *args, **options):
        war =  Book.objects.create(name = 'Война и Мир', author = 'Ф.Д. Достаевский', pub_date = '2021-03-05')
        dvor = Book.objects.create(name = 'Скотный Двор', author = 'Джордж Оруэл', pub_date = '2021-03-04')
        mind = Book.objects.create(name = 'В Память о прошлом земли', author = 'Лю Цысинь', pub_date = '2021-03-10')
        blink = Book.objects.create(name = 'Сияние', author = 'Cтивен Кинг', pub_date = '2021-03-11')
        test = Book.objects.create(name = '1984', author = 'Джордж Оруэл', pub_date = '2021-03-12')

        
        

        
