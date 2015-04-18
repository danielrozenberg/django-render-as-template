Render as Template
==================

A template tag for Django that takes a string and renders as it if it was a
template. Uses the current Engine and RequestContext.

Include in your template by adding ``{% load render_as_template %}``. Use by
adding ``{% render_as_template some_var %}`` where ``some_var`` is a context
variable that acts as a template.

Example: assume your view exposes two variables in the context: ``my_string``
and ``my_template``.

Then, if:

    ``my_string == u"http://example.com/"``, and

    ``my_template == u"Go to {{ my_string|urlize }}!""``, and

    ``the_views_template.html == u"{% render_as_template my_template %}"``

Then final output would be:

    ``Go to <a href="http://example.com/" rel="nofollow">http://example.com/</a>!``

Mixed with flatpages this lets you create powerful websites, although make sure
you trust the people who can edit those flatpages because who knows what kind
of dangerous security holes this thing will create! Also if your template
includes HTML don't forget to mark it safe:

    ``{% render_as_template my_template|safe %}``
