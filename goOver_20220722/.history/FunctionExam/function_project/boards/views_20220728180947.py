from django.shortcuts import render, redirect, get_object_or_404
from .models import Comments, Themes
from . import forms
from django.contrib import messages
from django.http import Http404
# #- キャッシュをimport
# from django.core.cache import cache
# #- jsonのレスポンス
# from django.http import JsonResponse

def create_theme(request):
    create_theme_form = forms.CreateThemeForm(request.POST or None)
    if create_theme_form.is_valid():
        #- Themesモデルは'accounts.Users'を外部キーとして持っているので、誰が作成したのかを設定する必要があるので、create_theme_form.save()の前にcreate_theme_form.instance.user=request.userとすると、現在ログインしてるユーザーを取得することができて、そのユーザーが作成したという風に外部キーを設定する必要がある!!
        #! 下記で現在ログインしているユーザ情報を取得する
        #- Exception Value:NOT NULL constraint failed: themes.user_idが下記の記述がないと起きる!
        create_theme_form.instance.user = request.user
        create_theme_form.save()
        messages.success(request, '掲示板を作成しました。')
        # return redirect('accounts:home')
        return redirect('boards:list_themes')
    return render(
        request, 'boards/create_theme.html', context={
            'create_theme_form':create_theme_form
        }
    )

def list_themes(request):
    #- class ThemesManager(models.Manager):経由で関数を取得
    themes = Themes.objects.fetch_all_themes()
    #- class ThemesManager(models.Manager):経由で関数を取得しなくても、問題なくフィルターや情報の抽出はできる。(models.Manager)を使う理由としては、後で管理を楽にするためだと思われる!
    # themes = Themes.objects.filter(id__gt = 3)
    return render(
        request, 'boards/list_themes.html', context={
            'themes': themes
        }
    )

def edit_theme(request, id):
    #- Themesの中の特定のinstanceをtheme.idで取得する
    theme = get_object_or_404(Themes, id=id)
    #- ログインしているユーザのidと編集しようとしているもののidが違う場合はエラーを起こす
    if theme.user.id != request.user.id:
        raise Http404
    #- 引数 instance=themeで編集する記事を特定している
    #- ModelFormでデータの更新をするには、Formの作成時にinstance=として、更新したいレコード を指定する。 forms.ModelForm(request.POST or None, instance=model)
    edit_theme_form = forms.CreateThemeForm(request.POST or None, instance=theme)
    if edit_theme_form.is_valid():
        edit_theme_form.save()
        messages.success(request, '掲示板を更新しました')
        return redirect('boards:list_themes')
    return render(
        request, 'boards/edit_theme.html',context={
            'edit_theme_form':edit_theme_form,
            'id':id,
        }
    )

def delete_theme(request, id):
    #- 値を取得する
    theme = get_object_or_404(Themes, id=id)
    if theme.user.id != request.user.id:
        raise Http404
    delete_theme_form = forms.DeleteThemeForm(request.POST or None)
    if delete_theme_form.is_valid(): # csrf checkを行う
        theme.delete()
        messages.success(request, '掲示板を削除しました')
        return redirect('boards:list_themes')
    return render(
        #- context={'delete_theme_form':delete_theme_form}はなくても問題なく動作する
        request, 'boards/delete_theme.html', context={
            'delete_theme_form':delete_theme_form,
        }
    )

def post_comments(request, theme_id):
    #- キャッシュがある場合はそれを取り出し、何もない場合は'' を取り出す => 何も取り出さない
    #! cache.set ではなく、 cache.getとする!
    #- キャッシュのデータを初期値とする
    post_comment_form = forms.PostCommentForm(request.POST or None)
    theme = get_object_or_404(Themes, id=theme_id)
    #- themeに対するコメントを取得する
    comments = Comments.objects.fetch_by_theme_id(theme_id)
    #- どのテーマ、誰のコメントなのかを取得する
    if post_comment_form.is_valid():
        if not request.user.is_au
        #- クラス属性で作業するインスタンスを保持できます。
        post_comment_form.instance.theme = theme
        post_comment_form.instance.user = request.user
        post_comment_form.save()
        #- 保存が成功したらキャッシュはいらなくなるので削除する
        #- redirect()には引数を渡せる ないと Exception Type:	NoReverseMatch のエラーが返ってくる 遷移先が見つからないため
        # return redirect('boards:post_comments') #! NG!!
        return redirect('boards:post_comments', theme_id=theme_id)
    return render(
        request, 'boards/post_comments.html', context={
            'post_comment_form': post_comment_form,
            'theme': theme,
            'comments': comments,
        }
    )


# def post_comments(request, theme_id):
#     #- キャッシュがある場合はそれを取り出し、何もない場合は'' を取り出す => 何も取り出さない
#     #! cache.set ではなく、 cache.getとする!
#     saved_comment = cache.get(f'saved_comment-theme_id={theme_id}-user_id={request.user.id}','')
#     #- キャッシュのデータを初期値とする
#     post_comment_form = forms.PostCommentForm(request.POST or None, initial={'comment': saved_comment})
#     #- どのテーマ、誰のコメントなのかを取得する
#     theme = get_object_or_404(Themes, id=theme_id)
#     comments = Comments.objects.fetch_by_theme_id(theme_id)
#     if post_comment_form.is_valid():
#         if not request.user.is_authenticated:
#             raise Http404
#         #- クラス属性で作業するインスタンスを保持できます。
#         post_comment_form.instance.theme = theme
#         post_comment_form.instance.user = request.user
#         post_comment_form.save()
#         #- 保存が成功したらキャッシュはいらなくなるので削除する
#         cache.delete(f'saved_comment-theme_id={theme_id}-user_id={request.user.id}')
#         return redirect('boards:post_comments', theme_id=theme_id)
#     return render(
#         request, 'boards/post_comments.html', context={
#             'post_comment_form': post_comment_form,
#             'theme': theme, 'comments':comments,
#         }
#     )

# #- キャッシュの操作(django.core.cache.cache)
# # cache.set(‘my_key’, ‘hello world!’) # my_keyにhello worldをキャッシュする
# # cache.get(‘my_key’, ‘default’) # my_keyに該当する値をキャッシュから取り出す。存在しない場合 は、defaultを返す
# # cache.clear() # キャッシュを全て削除する
# # cache.delete(‘a’) # キャッシュからaに該当するものを削除する

# def save_comment(request):
#     #- 原因：Django 4からはis_ajaxが使えなくなっている。
#     # if request.is_ajax:
#     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         comment = request.GET.get('comment')
#         theme_id = request.GET.get('theme_id')
#         if comment and theme_id:
#             cache.set(f'saved_comment-theme_id={theme_id}-user_id={request.user.id}',comment)
#             return JsonResponse({'message':'一時保存しました!'})