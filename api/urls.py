from django.urls import path,include
# from . import views
from .views import *
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     # path('books/', views.books_api, name='books'),
#     path('books/', ApiBooks.as_view(), name='books'),

#     # path('books/<pk>', views.book_api, name='book'),
#     path('books/<pk>', ApiBook.as_view(), name='book'),

#     # path('categorys/', views.categorys_api, name='categorys'),
#     path('categorys/', ApiCategorys.as_view(), name='categorys'),

#     # path('categorys/<pk>', views.category_api, name='category'),
#     path('categorys/<pk>', ApiCategory.as_view(), name='category'),
# ]


router = DefaultRouter()

router.register('books', Booksviewset)
router.register('categorys', CategorysViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('', include(router.urls)),
#     path('anything/',  anything_api, name='anything'),
# ]