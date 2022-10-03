from backend.models import *


class Profile(models.Model):
    ROLE_CHOICE = (
        (1, 'Admin'),
        (2, 'Usuario')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    role = models.IntegerField(choices=ROLE_CHOICE, max_length=1, blank=False, null=False, default=2)
    email = models.EmailField(blank=False, max_length=30, null=False, unique=True)
    active = models.BooleanField(default=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.user.username)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass
