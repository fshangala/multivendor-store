from rest_framework.routers import DefaultRouter
from stores.views import StoreViewSet

storesRouter=DefaultRouter()
storesRouter.register(r'stores',StoreViewSet,basename='stores')