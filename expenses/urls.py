from django.contrib import admin
from django.urls import path, include
# Import the redirect view
from django.views.generic import RedirectView

# ... other imports (router, views)

urlpatterns = [
    # Add a redirect for the root path
    path('', RedirectView.as_view(url='/users/', permanent=False)),
    
    path('admin/', admin.site.urls),
    # ... rest of your paths
    path('register/', RegisterUserView.as_view()),
    path('', include(router.urls)), # users endpoints
    path('expenses/summary/', ExpenseSummaryView.as_view()),
]