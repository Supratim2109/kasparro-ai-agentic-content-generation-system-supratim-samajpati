def render_faq(blocks):
    return {
        "page_type": "FAQ",
        "faqs":blocks["faq"][:5]
    }