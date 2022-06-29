from django.contrib import admin
from .models import Post#, MBO
from .models import MBO22,RHDT,ADC22,PDI22#,PDI22G

#admin.site.register(Post)
#admin.site.register(Account)
admin.site.register(MBO22)
admin.site.register(ADC22)
admin.site.register(PDI22)
admin.site.register(RHDT)

#admin.site.register(PDI22G)
