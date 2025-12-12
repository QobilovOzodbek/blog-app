from django.db import models
from django.utils.text import slugify
from django.urls import reverse

def default_image():
    return "default.jpg"   # media/default.jpg da bo'ladi


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


def default_image_path():
    return 'default.jpg'  # media/default.jpg ichida joylashgan bo‘lsin

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField()
    short_text = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True, default=default_image_path)
    tags = models.ManyToManyField(Tag, related_name="posts")
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # slug avtomatik
        if not self.slug:
            self.slug = slugify(self.title)
        # short_text avtomatik, post body'dan oladi
        if not self.short_text:
            self.short_text = self.body[:150] + '...'
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
    def __str__(self):
        return f"{self.title}"



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
