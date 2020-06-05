from django.contrib import admin
from .models import Post
from .models import Druzyna
from .models import Miejscowosc
from .models import Pilkarz
from .models import Mecz
from .models import Granie

admin.site.register(Post)
admin.site.register(Druzyna)
admin.site.register(Miejscowosc)
admin.site.register(Pilkarz)
admin.site.register(Mecz)
admin.site.register(Granie)