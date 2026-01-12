from django.core.management.base import BaseCommand
from online_store.models import Category, Product
import random
from faker import Faker

class Command(BaseCommand):
    help = 'Генерация данных'

    def handle(self, *args, **kwargs):
        self.stdout.write('Начинаем генерацию данных...')

        fake = Faker()
        categories = Category.objects.all()

        products = []
        for i in range(random.randint(5, 10)):
            product_name = fake.sentence(nb_words=6)
            product_category = random.choice(categories)
            product_description = fake.text(max_nb_chars=200)
            product_price = fake.pydecimal(left_digits=10, right_digits=2, positive=True)

            product = Product.objects.create(
                name=product_name,
                description=product_description,
                price=product_price,
                category=product_category
            )
            products.append(product)

        self.stdout.write(f'Создано {len(products)} товаров')
        self.stdout.write('Генерация данных завершена.')

