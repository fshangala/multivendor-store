from rest_framework.routers import DefaultRouter
from chats.views import OrderMessagesViewSet

chatsRouter=DefaultRouter()
chatsRouter.register(r'order-messages',viewset=OrderMessagesViewSet,basename='order-messages')