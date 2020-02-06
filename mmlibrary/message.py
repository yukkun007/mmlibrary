from jinja2 import Environment, FileSystemLoader


class Message(object):

    TEMPLATE_ROOT_DIR = "mmlibrary/template"

    @staticmethod
    def create(template_path, data) -> str:
        env = Environment(loader=FileSystemLoader(Message.TEMPLATE_ROOT_DIR))
        template = env.get_template(template_path)
        message = template.render(data)
        return message
