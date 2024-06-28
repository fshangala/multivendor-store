from rest_framework.routers import DefaultRouter
from orders.views import OrderViewSet

ordersRouter=DefaultRouter()
ordersRouter.register(r'orders',viewset=OrderViewSet,basename='orders')