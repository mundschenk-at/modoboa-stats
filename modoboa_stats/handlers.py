"""Modoboa stats signal handlers."""

from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.utils.translation import ugettext as _

from modoboa.core import signals as core_signals

from . import graphics
from . import signals


@receiver(core_signals.extra_user_menu_entries)
def menu(sender, location, user, **kwargs):
    """Return extra menu entry."""
    if location != "top_menu" or user.role == "SimpleUsers":
        return []
    return [
        {"name": "stats",
         "label": _("Statistics"),
         "url": reverse('modoboa_stats:fullindex')}
    ]


@receiver(signals.get_graph_sets)
def get_default_graphic_sets(sender, **kwargs):
    """Return graphic set."""
    gset = graphics.MailTraffic()
    return {gset.html_id: gset}
