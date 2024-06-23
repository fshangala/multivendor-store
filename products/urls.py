from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, StockViewSet

productsRouter=DefaultRouter()
productsRouter.register(r'products',ProductViewSet,basename='products')
productsRouter.register(r'stocks',StockViewSet,basename='stocks')