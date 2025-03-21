import inspect
import os


class MetaTemplated(type):

    def __new__(cls, cls_name, cls_parents, cls_attrs):
        rv = type.__new__(cls, cls_name, cls_parents, cls_attrs)
        
        # check if template file exists
        assert hasattr(rv, 'template_html'), f'Class {cls_name} is missing template_html attribute.'
        path = os.sep.join([os.path.dirname(inspect.getfile(rv)), rv.template_html])
        assert os.path.exists(path), f'Template {rv.template_html} does not exist.'
        rv.abs_template_html = path
        
        # check if js template exists
        assert hasattr(rv, 'template_js'), f'Class {cls_name} is missing template_js attribute.'
        path = os.sep.join([os.path.dirname(inspect.getfile(rv)), rv.template_js])
        assert os.path.exists(path), f'Template {rv.template_js} does not exist.'
        rv.abs_template_js = path

        return rv


class MetaArg(MetaTemplated):
    registry = dict()

    def __new__(cls, cls_name, cls_parents, cls_attrs):
        rv = super().__new__(cls, cls_name, cls_parents, cls_attrs)
        
        # check if exists
        assert cls_name not in cls.registry.keys(), f'Class {cls_name} has already been registered.'
        
        # check maping mechanism exists
        assert hasattr(rv, 'map')
        assert hasattr(rv, 'maps_to')
        
        # register class
        cls.registry[cls_name] = rv
        print(f"Argument class {cls_name} registered successfully.")
        return rv

    @classmethod
    def __getitem__(cls, key):
        return cls.registry[key]
