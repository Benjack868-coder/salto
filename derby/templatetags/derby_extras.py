from django import template
from derby.models import Entry, Fight

register = template.Library()


@register.filter(name='derby_type')
def derby_type(value, **kwargs):
    if int(value) is 1:
        d_type = 'Stag'
    elif int(value) is 2:
        d_type = 'Bullstag',
    elif int(value) is 3:
        d_type = 'Cock'
    return d_type


@register.filter(name='derby_total_participants')
def derby_total_participants(value, **kwargs):
    count = Entry.objects.filter(tournament_id=value).count()
    return count


@register.filter(name='derby_total_entry')
def derby_total_entry(value, **kwargs):
    fight = Fight.objects.filter(tournament_id=value).count()
    return fight


@register.filter(name='derby_total_bet')
def derby_total_bet(value, **kwargs):
    total = 0
    fights = Fight.objects.filter(tournament_id=value)
    for fight in fights:
        total += fight.bet
    return float(total)


@register.filter(name='total_entry')
def total_entry(id, **kwargs):
    total = 0
    total = Fight.objects.filter(owner_id=id).count()
    return total
