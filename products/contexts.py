from django.core.cache import cache


def cached_queries(request):
    context = {
        'cache': cache.get('products_filtered_cache')
    }
    return context
