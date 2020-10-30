from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationManual(PageNumberPagination):
    # 默认第几页p,默认两条数据
    page_query_param = 'p' # 页数
    page_size = 2

    page_size_query_param = 's' # 每页数量
    max_page_size = 50  # 前端最大指定
