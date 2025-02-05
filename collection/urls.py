from django.urls import path, include
from collection.views import (show_collection, forum_archive, education_archive, get_json, get_forum_json, get_education_json)

app_name = 'collection'

urlpatterns = [
    path('', show_collection, name='show_collection'),
    path('json/', get_json, name='json'),
    path('forum/', forum_archive, name='forum'),
    path('forum/json/', get_forum_json, name='forum_json'),
    path('education/', education_archive, name='education'),
    path('education/json/', get_education_json, name='education_json'),
    path('forum/items/', include('forum_item.urls'), name='collection_forum_items'),
    # TODO ADD EDUC
]