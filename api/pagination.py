"""
Custom pagination class for consistent page size handling in API responses.
"""

from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    """
    Standard pagination configuration using page numbers.

    - Default page size: 20 results per page
    - Client can override using `?page_size=` query param
    - Maximum allowed page size: 100
    """

    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 100
