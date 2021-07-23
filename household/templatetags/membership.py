from django import template

register = template.Library()

@register.filter
def level_name(member, family):
    membership = member.membership_set.get(family=family)
    level = membership.command_level
    name = membership.CommandLevel(level).name

    capitalized_name = name.capitalize()
    
    formated_name = capitalized_name.replace("_", " ")

    return formated_name

@register.filter
def command_level(member, family):
    membership = member.membership_set.get(family=family)
    level = membership.command_level

    return level
