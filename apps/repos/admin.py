from django.contrib import admin

from apps.repos.models import GithubRepositories, RepositoryContributors


@admin.register(GithubRepositories)
class GithubRepositories(admin.ModelAdmin):
    pass


@admin.register(RepositoryContributors)
class GithubRepositories(admin.ModelAdmin):
    pass
