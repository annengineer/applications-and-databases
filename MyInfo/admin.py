from django.contrib import admin

from .models import Members

admin.site.register(Members)

from .models import Management

admin.site.register(Management)

from .models import EP

admin.site.register(EP)