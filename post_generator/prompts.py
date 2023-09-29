# Importing style definitions from an external module
from post_generator.style import default_writting_style_definitions

class Prompts:

    """This method returns a string containing guidelines for avoiding certain types of content in prompts,
        such as emojis, up-to-date information, false data, or mentions of real links or offered products/services."""
    @staticmethod
    def get_avoids():
        return "\n\nNote: avoid including any emojis, text or ideas which requires up-to-date information,or which could contain false data, or which mentions a real link or offered product/service"
    
    """This method takes a list of style items as input and constructs a style prompt by concatenating
        these items together."""
    def build_style_prompt(style_items: str):
        return '\n\nFollow these style guidelines:' + ', '.join(style_items)
