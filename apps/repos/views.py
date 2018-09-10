import json

from django.http import JsonResponse

from apps.repos.models import GithubRepositories, RepositoryContributors


def save_search_data(request):
    if request.method == 'POST':
        contributer_statistic = json.loads(request.POST.get('contributer_statistic'))
        repo_info = json.loads(request.POST.get('repo_info'))
        new_repo = GithubRepositories(
            user=request.user,
            name=repo_info['name'],
            url=repo_info['url'],
        )
        new_repo.save()
        contribs = json.loads(request.POST.get('all_contrib'))

        for x in contribs:
            login = x['login']

            if login in contributer_statistic:
                if (contributer_statistic[login]['percent']):
                    percent = contributer_statistic[login]['percent']
                else:
                    percent = None

            new_contrib = RepositoryContributors(
                repository=new_repo,
                login=login,
                last_hundred_actions_percent=percent
            )

            new_contrib.save()
    return JsonResponse(status=200, data={"success": True})
