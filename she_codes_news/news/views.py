from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory, Comment
from .forms import StoryForm, CommentForm
from users.models import CustomUser
from django.shortcuts import render, get_object_or_404


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all()
        return context


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm
        context["comments"] = Comment.objects.order_by('-created_date')
        return context


class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_story_view'] = True
        return context

    def form_valid(self, form):
        # this means to set the author as the user currently logged in
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditStoryView(generic.edit.UpdateView):
    form_class = StoryForm
    model = NewsStory
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_story_view'] = False
        return context

    def get_queryset(self):
        return NewsStory.objects.all()


class AddCommentView(generic.CreateView):
    form_class = CommentForm
    template_name = 'news/createComment.html'
    context_object_name = 'comments'

    def form_valid(self, form):
        form.instance.author = self.request.user
        pk = self.kwargs.get("pk")
        story = get_object_or_404(NewsStory, pk=pk)
        form.instance.story = story
        return super().form_valid(form)

    def get_queryset(self):
        return Comment.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.order_by('-created_date')
        return context

    def get_success_url(self) -> str:
        pk = self.kwargs.get("pk")
        return reverse_lazy("news:story", kwargs={'pk':pk})


# ----- simple success page to confirm deletion of story ----- 
def delete_success_view(request):
    return render(request, 'news/deleteSuccess.html')


class DeleteStoryView(generic.edit.DeleteView):
    model = NewsStory
    template_name = 'news/deleteView.html'
    success_url = reverse_lazy('news:deleteSuccess')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['story'] = NewsStory.objects.get(id=self.kwargs['pk'])
        return context


# new class for viewing authors stories
class AuthorStories(generic.ListView):
    template_name = 'news/authorStories.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.filter(author_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.filter(author_id=self.kwargs['pk'])
        context['author'] = CustomUser.objects.get(id=self.kwargs['pk'])
        return context
