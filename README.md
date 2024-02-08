# CostaPy Template - EzMail
A simple CostaPy email template.
Email template create by [Colorlib](https://github.com/ColorlibHQ/email-templates/tree/master/10).

## Usage

- Put the folder in your templates directory
- Add to handler

        import templates.ezmail.main as ezmail

        kwargs["mako"] = {
          "email" : ezmail.main(directory.page["email"], "verification") # page_directory, file_name
        }

- Define a necessary variable on your modules function

        title       = "CostaPy"
        heading     = title
        image       = "https://sample.com/logo.png"
        unsubscribe = "https://sample.com/unsubscribe"

        message     = "Please verify your email"
        link        = "https://sample.com/verify"

- Set a template on your modules function

        from mako.template import Template

        interface = Template(params["mako"]["email"]['template']).render(
          title       = title,
          heading     = heading,
          image       = image,
          unsubscribe = unsubscribe,
          container = Template(params["mako"]["email"]['container']).render(
            message   = message,
            link      = link
          )
        )
