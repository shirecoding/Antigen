import glob
import os

from jinja2 import Environment, FileSystemLoader, PackageLoader, Template

from .utils import files_in_folder, stdout_logger, components_dir

log = stdout_logger(__name__)

jinja_env = Environment(loader=FileSystemLoader(components_dir))

###############################################################################
## Blueprint
###############################################################################


def component_is_valid(component):

    if "component" not in component:
        log.warning("component field missing in definition")
        return False

    fields = ["component", "id", "props", "children"]
    for f in fields:
        if f not in component:
            log.warning(f"{f} missing in component: {component['component']}")
            return False
    return True


def create_component(component: dict, path: str, templates: str) -> str:
    """
    Args:
        component: component definition ('component', 'id', 'props', 'children' keys are used in generation)
        path: path to create component js file
        templates: path to template folder

    Returns:
        str: path to component js file
    """

    if os.path.isfile(path):
        raise Exception(f"{path} already exists")

    if not component_is_valid(component):
        raise Exception(f"invalid component")

    templates = jinja_env.list_templates()
    log.debug(templates)

    if f"{component['component']}.js" in templates:
        template = f"{component['component']}.js"
    elif "Default.js" in templates:
        log.debug(f"no template found for f{component['component']} using Default.js")
        template = "Default.js"
    else:
        raise Exception(f"no component templates found for {component['component']}")

    with open(path, "w") as f:
        log.debug(f"Generating template {template} -> {path} ...")
        f.write(
            jinja_env.get_template(template).render(
                id=component["id"],
                component=component["component"],
                children=component["children"],
                props=component["props"],
            )
        )

    return path
