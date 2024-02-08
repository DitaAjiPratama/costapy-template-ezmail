from core   import html

static = []

def main(dir, page):

    html_template   = html.main.get_html("templates/ezmail/html")
    html_page       = html.main.get_html(dir)
    params_list = {
        "template"  : html_template ["template.html"    ]   ,
        "container" : html_page     [ page+".html"      ]
    }
    return params_list
