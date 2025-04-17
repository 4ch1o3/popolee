from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer



class FeedPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'limit'

class Api_feed(ListAPIView):
    serializer_class = PostSerializer
    pagination_class = FeedPagination

    def get_queryset(self):

        #default sort option is 'like'
        sort_option = self.request.query_params.get('sort')
        if not sort_option:
            sort_option = 'like'

        match sort_option:
            case 'like':
                sort_field = '-likecount'
            case 'old':
                sort_field = 'created_at'
            case 'new':
                sort_field = '-created_at'

        #tag : headcount
        headcount = self.request.query_params.get('headcount')
        if headcount:
            queryset = Post.objects.all().filter(headcount=headcount).order_by(sort_field)
        else:
            queryset = Post.objects.all().order_by(sort_field)
        
        return queryset



