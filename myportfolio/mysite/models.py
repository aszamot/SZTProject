from django.db import models


class About(models.Model):
    greetings_text = models.CharField(max_length=50)
    description_text = models.TextField()
    image = models.ImageField(upload_to='images/about/', blank=True, null=True)


class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/skill/', blank=True, null=True)
    is_on_main = models.BooleanField()


class Recommendation(models.Model):
    image = models.ImageField(upload_to='images/recommendation')
    recommendation_name = models.CharField(max_length=60)
    recommendation_company = models.CharField(max_length=40)
    recommendation_text = models.TextField()


class Article(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    date = models.DateField()


class Art(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images/art_thumbs', blank=True, null=True)


class ArtImage(models.Model):
    art = models.ForeignKey(Art, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='images/art/')


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    github_url = models.CharField(max_length=200, null=True, blank=True)
    project_url = models.CharField(max_length=200, null=True, blank=True)
    logo_image = models.ImageField(upload_to='images/projects_logo/', blank=True, null=True)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='images/projects/')
