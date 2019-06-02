import xadmin
from xadmin import views

from . import models


class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True


class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "Xadmin"  # 设置站点标题
    site_footer = "个人博客"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)


# 文章
class ArticleAdmin(object):
    model_icon = 'fa fa-book'
    date_hierarchy = 'create_date'
    exclude = ['views']
    list_display = ['id', 'title', 'author', 'create_date', 'update_date', 'views']
    list_editable = ['id', 'title', 'author', 'create_date', 'update_date']
    list_display_links = ['title']
    list_filter = ['create_date', 'category', 'tags', 'keywords']
    list_per_page = 50  # 控制每页显示的对象数量，默认是100
    filter_horizontal = ['tags', 'keywords']
    search_fields = ['id', 'title', 'author']
    show_detail_fields = ['id']
    style_fields = {"content": "ueditor"}
    show_bookmarks = True
    list_export = ['xls', 'csv', 'xml']
    list_export_fields = ['title', 'body']
    refresh_times = [1000, 5000]  # 可选以支持按多长时间(秒)刷新页面
    data_charts = {
        'views': {'title': '阅览量', "x-field": "create_date", "y-field": ('views',), "order": ('create_date',)}
    }

    # import_excel = True
    #
    # def post(self, request, *args, **kwargs):
    #     if 'excel' in request.FILES:
    #         pass
    #     # 必须返回，不然报错（或者注释掉）
    #     return super(ArticleAdmin, self).post(request, *args, **kwargs)


xadmin.site.register(models.Article, ArticleAdmin)


# 文章标签
class TagAdmin(object):
    model_icon = 'fa fa-tag'
    list_display = ['name', 'id', 'slug']


xadmin.site.register(models.Tag, TagAdmin)


# 导航栏，分类下的下拉擦菜单分类
class CategoryAdmin(object):
    model_icon = 'fa fa-circle-o'
    list_display = ['name', 'id', 'slug']


xadmin.site.register(models.Category, CategoryAdmin)


# 网站导航菜单栏分类表
class BigCategoryAdmin(object):
    model_icon = 'fa fa-star'
    list_display = ['name', 'id', 'slug']


xadmin.site.register(models.BigCategory, BigCategoryAdmin)


# 幻灯片
class CarouselAdmin(object):
    model_icon = 'fa fa-picture-o'
    list_display = ['number', 'title', 'content', 'img_url', 'url']


xadmin.site.register(models.Carousel, CarouselAdmin)


class KeywordAdmin(object):
    model_icon = 'fa fa-key'
    list_display = ['name', 'id']


xadmin.site.register(models.Keyword, KeywordAdmin)


# 友情链接表
class FriendLinkAdmin(object):
    model_icon = 'fa fa-link'
    list_display = ['name', 'description', 'link', 'create_date', 'is_active', 'is_show']
    list_editable = ['name', 'description', 'link', 'create_date', 'is_active', 'is_show']
    date_hierarchy = 'create_date'
    list_filter = ['is_active', 'is_show']


xadmin.site.register(models.FriendLink, FriendLinkAdmin)
