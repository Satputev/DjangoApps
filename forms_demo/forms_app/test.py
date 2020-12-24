from django.core.paginator import Paginator
ls=[1,2,3]
ref=Paginator(ls,1)
d=ref.page(1)
print(d)
print()