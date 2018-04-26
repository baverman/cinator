from jinja2 import Environment, FileSystemLoader

loader = FileSystemLoader('template')
jinja_env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
