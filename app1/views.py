from django.shortcuts import render, HttpResponse, redirect
from app1 import models


# Create your views here.
# 查询出版社列表
def publisher_list(request):
    res = models.Publisher.objects.all().order_by('-id')        # -id降序，id默认升序，加‘-’为降序
    # for item in res:
    #     print(item.id, ': ', item.name, item)
    return render(request, 'publisher/publisher_list.html', {'publisherList': res})


# 新增出版社名称
def publisher_add(request):
    if request.method == 'GET':
        return render(request, 'publisher/publisher_add.html')
    elif request.method == 'POST':
        pub_name = request.POST.get('pub_name')
        if not pub_name:
            return render(request, 'publisher/publisher_add.html', {'msg': '出版社名称不能为空'})
        res = models.Publisher.objects.filter(name=pub_name)
        if not res:     # 出版社不存在
            models.Publisher.objects.create(name=pub_name)      # 创建出版社
            return redirect('/app/publisher_list/')
        return render(request, 'publisher/publisher_add.html', {'msg': '出版社名称已存在'})
    return render(request, 'publisher/publisher_add.html', {'msg': '请求错误'})


# 修改出版社名称
def publisher_update(request):
    if request.method == 'GET':
        ppk = request.GET.get('pk')
        if not ppk:     # 未取到主键
            return render(request, 'publisher/publisher_update.html', {'msg': '请求错误'})
        res = models.Publisher.objects.filter(pk=ppk)
        if not res:
            return render(request, 'publisher/publisher_update.html', {'msg': '请求错误'})
        else:
            return render(request, 'publisher/publisher_update.html', {'pub_obj': res[0]})
    elif request.method == 'POST':
        ppk = request.GET.get('pk')
        pub_name = request.POST.get('pub_name')
        if not ppk:                         # 未取到主键或出版社名称
            return render(request, 'publisher/publisher_update.html', {'msg': '请求出错'})
        if not pub_name:                    # 未取到出版社名称
            return render(request, 'publisher/publisher_update.html', {'msg': '出版社名称不能为空'})
        res = models.Publisher.objects.filter(pk=ppk)
        if not res:
            return render(request, 'publisher/publisher_update.html', {'msg': '修改出错'})
        elif models.Publisher.objects.filter(name=pub_name):
            return render(request, 'publisher/publisher_update.html', {'msg': '出版社已存在', 'pub_obj': res[0]})
        else:
            pub_obj = res[0]
            pub_obj.name = pub_name     # 修改出版社名称
            pub_obj.save()              # 保存至数据库
            return redirect('/app/publisher_list/')
    return render(request, 'publisher/publisher_update.html', {'msg': '请求错误'})


# 删除出版社
def publisher_delete(request):
    ppk = request.GET.get('pk')
    models.Publisher.objects.filter(pk=ppk).delete()        # 执行删除
    return redirect('/app/publisher_list/')


# 查询作者列表
def author_list(request):
    res = models.Author.objects.all().order_by('-id')        # -id降序，id默认升序，加‘-’为降序
    # author1 = res[0]
    # print(author1)
    # print(author1.pk)
    # print(author1.book_set.all())
    # for item in res:
    #     print(item.id, ': ', item.name, item)
    return render(request, 'author/author_list.html', {'authorList': res})


# 新增作者
def author_add(request):
    if request.method == 'GET':
        return render(request, 'author/author_add.html')
    elif request.method == 'POST':
        pub_name = request.POST.get('auth_name')
        if not pub_name:
            return render(request, 'author/author_add.html', {'msg': '作者名称不能为空'})
        res = models.Author.objects.filter(name=pub_name)
        if not res:                     # 作者不存在
            models.Author.objects.create(name=pub_name)      # 创建作者
            return redirect('/app/author_list/')
        return render(request, 'author/author_add.html', {'msg': '作者已存在'})
    return render(request, 'author/author_add.html', {'msg': '请求错误'})


# 修改作者名称
def author_update(request):
    if request.method == 'GET':
        ppk = request.GET.get('pk')
        if not ppk:                         # 未取到主键
            return render(request, 'author/author_update.html', {'msg': '请求错误'})
        res = models.Author.objects.filter(pk=ppk)
        if not res:
            return render(request, 'author/author_update.html', {'msg': '请求错误'})
        else:
            return render(request, 'author/author_update.html', {'auth_obj': res[0]})
    elif request.method == 'POST':
        ppk = request.GET.get('pk')
        auth_name = request.POST.get('auth_name')
        if not ppk:                             # 未取到主键或作者名称
            return render(request, 'author/author_update.html', {'msg': '请求出错'})
        if not auth_name:                       # 未取到作者名称
            return render(request, 'author/author_update.html', {'msg': '作者名称不能为空'})
        res = models.Author.objects.filter(pk=ppk)
        if not res:
            return render(request, 'author/author_update.html', {'msg': '修改出错'})
        elif models.Author.objects.filter(name=auth_name):
            return render(request, 'author/author_update.html', {'msg': '作者已存在', 'auth_obj': res[0]})
        else:
            auth_obj = res[0]
            auth_obj.name = auth_name           # 修改出版社名称
            auth_obj.save()                     # 保存至数据库
            return redirect('/app/author_list/')
    return render(request, 'author/author_update.html', {'msg': '请求错误'})


# 删除出版社
def author_delete(request):
    ppk = request.GET.get('pk')
    models.Author.objects.filter(pk=ppk).delete()        # 执行删除
    return redirect('/app/author_list/')


# 展示书籍列表
def book_list(request):
    all_books = models.Book.objects.all().order_by('id')
    return render(request, 'book/book_list.html', {'all_books': all_books})


# 新增书籍
def book_add(request):
    all_publishers = models.Publisher.objects.all()
    all_authors = models.Author.objects.all()
    if request.method == 'GET':
        return render(request, 'book/book_add.html', {'all_publishers': all_publishers, 'all_authors': all_authors})
    elif request.method == 'POST':
        bk_name = request.POST.get('name')
        pub_id = request.POST.get('pub_id')
        auth_ids = request.POST.getlist('auth_ids')
        if bk_name and pub_id and auth_ids:
            if models.Book.objects.filter(name=bk_name):
                return render(request, 'book/book_add.html', {'all_publishers': all_publishers, 'all_authors': all_authors, 'msg': '图书已存在'})
            else:
                book = models.Book.objects.create(name=bk_name, publisher_id=pub_id)    # 新增图书
                book.authors.set(auth_ids)                  # 多对多关系的维护
                return redirect('/app/book_list/')
        else:
            return render(request, 'book/book_add.html', {'all_publishers': all_publishers, 'all_authors': all_authors, 'msg': '书名不能为空'})
    return render(request, 'book/book_add.html', {'all_publishers': all_publishers, 'all_authors': all_authors, 'msg': '请求错误'})


# 修改书籍
def book_update(request):
    all_publishers = models.Publisher.objects.all()         # 查询所有的出版社
    all_authors = models.Author.objects.all()               # 查询所有的作者
    bk_id = request.GET.get('bk')                           # 从URL中取出bk_id
    books = models.Book.objects.filter(pk=bk_id)            # 查找过滤书籍
    book = books[0]
    if request.method == 'GET' and bk_id:                   # GET 请求并且传参
        return render(request, 'book/book_update.html', {'all_publishers': all_publishers, 'book': book, 'all_authors': all_authors})
    elif request.method == 'POST':                          # POST请求
        bk_name = request.POST.get('name')
        pub_id = request.POST.get('pub_id')
        auth_ids = request.POST.getlist('auth_ids')
        if bk_name and pub_id:                              # 获取到书名和出版社ID
            if models.Book.objects.filter(name=bk_name):    # 书名已存在
                bk_auths = models.Book.objects.get(name=bk_name).authors.all()
                bk_auth_ids = [bk_auth.pk for bk_auth in bk_auths]      # 将对象列表的ID转换成里列表
                if bk_auth_ids == auth_ids:
                    return render(request, 'book/book_update.html', {'all_publishers': all_publishers, 'book': book, 'all_authors': all_authors, 'msg': '图书已存在'})
            models.Book.objects.filter(pk=bk_id).update(name=bk_name, publisher_id=pub_id)      # 执行更新（只更新指定字段），比 对象.save() 高效
            book.authors.set(auth_ids)                      # 维护多对多关系
            return redirect('/app/book_list/')
        else:
            return render(request, 'book/book_update.html', {'all_publishers': all_publishers, 'book': book, 'all_authors': all_authors, 'msg': '书名不能为空'})
    return render(request, 'book/book_update.html', {'all_publishers': all_publishers, 'all_authors': all_authors, 'msg': '请求错误'})


# 删除书籍
def book_delete(request):
    bk_id = request.GET.get('bk')                       # 从URL中取出bk_id
    models.Book.objects.filter(pk=bk_id).delete()       # 执行删除
    return redirect('/app/book_list/')                  # 重定向到图书列表

