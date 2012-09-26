from django.db.models import Q
from django.db.models.sql.query import get_order_dir


def get_next_or_previous(qs, item, next=True):
    """
    Get the next or previous object in the queryset, with regards to the
    item specified.
    """
    # If we want the previous object, reverse the default ordering
    if next:
        default_ordering = 'ASC'
    else:
        default_ordering = 'DESC'

    # First, determine the ordering. This code is from get_ordering() in
    # django.db.sql.compiler
    if qs.query.extra_order_by:
        ordering = qs.query.extra_order_by
    elif not qs.query.default_ordering:
        ordering = qs.query.order_by
    else:
        ordering = qs.query.order_by or qs.query.model._meta.ordering

    assert not ordering == '?', 'This makes no sense for random ordering.'

    query_filter = None
    for field in ordering:
        item_value = getattr(item, field)

        # Account for possible reverse ordering
        field, direction = get_order_dir(field, default_ordering)

        # Either make sure we filter increased values or lesser values
        # depending on the sort order
        if direction == 'ASC':
            filter_dict = {'%s__gt' % field: item_value}
        else:
            filter_dict = {'%s__lt' % field: item_value}

        # Make sure we nicely or the conditions for the queryset
        if query_filter:
            query_filter = query_filter | Q(**filter_dict)
        else:
            query_filter = Q(**filter_dict)

    # Reverse the order if we're looking for previous items
    if default_ordering == 'DESC':
        qs = qs.reverse()

    # Filter the queryset
    qs = qs.filter(query_filter)

    # Return either the next/previous item or None if not existent
    try:
        return qs[0]
    except IndexError:
        return None
