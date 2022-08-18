from menu.models import *

u1 = User(email='nikname21@gmail.com', password='defender42')
u1.save()
c1 = Client(user=u1, name='Азат Соколов', card_number = '4147 5657 9878 9009')
c1.save()
u2 = User(email='altywa1998@gmail.com', password='nono34')
u2.save()
w1 = Worker(user=u2, name='Алтынай Алиева', position='работник кассы')
w1.save()
f1 = Food.objects.create(name='шаурма', start_price=50)
f2 = Food.objects.create(name='гамбургер', start_price=25)
i1 = Ingredient.objects.create(name='сыр', extra_price=10)
i2 = Ingredient.objects.create(name='курица', extra_price=70)
i3 = Ingredient.objects.create(name='горядина', extra_price=80)
i4 = Ingredient.objects.create(name='салат', extra_price=15)
i5 = Ingredient.objects.create(name='фри', extra_price=15)

o1 = Order(food=f1, ingredient=i3, client=c1, worker=w1)
o2 = Order(food=f1, ingredient=i1, client=c1, worker=w1)
o3 = Order(food=f1, ingredient=i4, client=c1, worker=w1)
o4 = Order(food=f1, ingredient=i5, client=c1, worker=w1)

o5 = Order(food=f2, ingredient=i2, client=c1, worker=w1)
o6 = Order(food=f2, ingredient=i4, client=c1, worker=w1)

o1.save()
o2.save()
o3.save()
o4.save()
o5.save()
o6.save()

order_sha = Order.objects.filter(client__name='Азат Соколов', worker__name='Алтынай Алиева', food__name='шаурма')
order_ham = Order.objects.filter(client__name='Азат Соколов', worker__name='Алтынай Алиева', food__name='гамбургер')


final_price_sha = order_sha.first().food.start_price
for o in order_sha:
    final_price_sha += o.ingredient.extra_price

final_price_ham = order_ham.first().food.start_price
for o in order_ham:
    final_price_ham += o.ingredient.extra_price

order_price = final_price_ham + final_price_sha

print(final_price_ham)
print(final_price_sha)
print(order_price)