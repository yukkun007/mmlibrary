import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


class Message(object):
    @staticmethod
    def _get_template_root_dir() -> str:
        path = Path(os.path.abspath(__file__))
        return str(path.parent.joinpath("template"))

    @staticmethod
    def create(template_path, data) -> str:
        env = Environment(loader=FileSystemLoader(Message._get_template_root_dir()))
        template = env.get_template(template_path)
        message = template.render(data)
        return message
