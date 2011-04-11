from django import template

register = template.Library()

class ModuleNode(template.Node):
    def __init__(self, module_name):
        self.module_name = module_name

    def render(self, context):
        if self.module_name == 'member_points_box':
            from empcom.points import fetch_points_box
            return fetch_points_box(context)
        return self.module_name

@register.tag(name="module")
def get_module(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, module_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]
    if not (module_name[0] == module_name[-1] and module_name[0] in ('"', "'")):
        raise template.TemplateSyntaxError, "%r tag's argument should be in quotes" % tag_name
    return ModuleNode(module_name[1:-1])
