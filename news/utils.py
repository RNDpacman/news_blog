from django.contrib.auth.mixins import UserPassesTestMixin
from antiblog import settings

class IsPermitGroupMixin(UserPassesTestMixin):
    mixin_prop = ''
    groups = settings.GROUPS_PERMIT_ADD_NEWS
    from antiblog import settings
    
    def is_in_groups(self, groups):
        return self.request.user.groups.filter(name__in=groups).exists()
    
    def test_func(self):
        return self.is_in_groups(self.groups)
    
    

    