from jinja2 import Template
import os


class View:
    def __init__(self, request, context) -> None:
        self.req = request
        self.name = "template.html"
        self.context = context
        self.rendered = ""

    def setContext(self, context):
        self.context = context

    def setName(self, name):
        self.name = name

    def render(self) -> str:
        file = open(self.name)
        t = Template(file.read())
        rendered = t.render(self.context)
        file.close()
        self.rendered = rendered
        return rendered

    def getRendered(self) -> str:
        return self.rendered
