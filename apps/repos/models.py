from django.db import models

from apps.users.models import User


class GithubRepositories(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    url = models.URLField(null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Github Repositories"


class RepositoryContributors(models.Model):
    repository = models.ForeignKey(GithubRepositories, on_delete=models.CASCADE, null=False, blank=False)

    login = models.CharField(max_length=255, null=False, blank=False)
    last_hundred_actions_percent = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name_plural = "Repository Contributors"
