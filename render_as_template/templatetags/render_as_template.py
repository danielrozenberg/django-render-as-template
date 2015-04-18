from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def render_as_template(context, template_as_string):
    template_as_object = context.template.engine.from_string(template_as_string)
    return template_as_object.render(context)
