
def set_category_actions(value,label):
    def category_actions(modeladmin,request,queryset):
        queryset.update(category = value)
    category_actions.short_description = f"Set Category {label}"
    return category_actions

def set_tag_actions(value,label):
    def tag_actions(modeladmin,request,queryset):
        queryset.update(tag = value)
    tag_actions.short_description = f"Set Tag {label}"
    return tag_actions

def set_brand_actions(value,label):
    def brand_action(modeladmin,request,queryset):
        queryset.update(brand = value)
    brand_action.short_decription = f"Set Brand {label}"
    return brand_action