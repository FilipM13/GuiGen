import inspect
import os


class MetaTemplated(type):
    all_templates: set["MetaTemplated"] = set()

    def __new__(cls, cls_name, cls_parents, cls_attrs):
        rv = type.__new__(cls, cls_name, cls_parents, cls_attrs)

        # check if template file exists
        assert hasattr(
            rv, "template_html"
        ), f"Class {cls_name} is missing template_html attribute."
        if "template_html" in cls_attrs.keys():
            path = os.sep.join([os.path.dirname(inspect.getfile(rv)), rv.template_html])
            assert os.path.exists(path), f"Template {path} does not exist."
            rv.abs_template_html = path

        # copy extra templates
        if hasattr(rv, "templates_extra"):
            for i, te in enumerate(rv.templates_extra):
                rv.templates_extra[i] = (
                    os.sep.join([os.path.dirname(inspect.getfile(rv)), te]),
                    te,
                )

        cls.all_templates.add(rv)

        return rv


class MetaArg(MetaTemplated):
    registry: dict[str, "MetaArg"] = dict()

    def __new__(cls, cls_name, cls_parents, cls_attrs):
        rv = super().__new__(cls, cls_name, cls_parents, cls_attrs)

        # check if exists
        assert (
            cls_name not in cls.registry.keys()
        ), f"Class {cls_name} has already been registered."

        # check maping mechanism exists
        assert hasattr(rv, "map")
        assert hasattr(rv, "maps_to")

        # register class
        cls.registry[cls_name] = rv
        print(f"Argument class {cls_name} registered successfully.")
        return rv

    @classmethod
    def __getitem__(cls, key):
        return cls.registry[key]


class __main__(metaclass=MetaTemplated):
    template_html = "templates/__main__.jinja2"
    templates_extra = ["templates/style.css", "templates/__main__js.jinja2"]
