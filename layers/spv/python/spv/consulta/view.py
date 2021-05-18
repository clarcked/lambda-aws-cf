from jinja2 import Template


class View:
    def __init__(self, request, name, params={}) -> None:
        self.req = request
        self.name = name
        self.params = params
        self.rendered = self.render()

    def render(self) -> str:
        file = open(self.name)
        t = Template(file.read())
        rendered = t.render(self.params)
        file.close()
        return rendered

    def getRendered(self) -> str:
        return self.rendered
