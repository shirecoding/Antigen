import logging
import os
import shutil
import sys

import yaml

###############################################################################
## Important Paths
###############################################################################

module_dir = os.path.dirname(sys.modules["antigen"].__file__)
resources_dir = os.path.join(module_dir, "resources")
components_dir = os.path.join(resources_dir, "components")
examples_dir = os.path.join(resources_dir, "examples")

###############################################################################
## General
###############################################################################


def read_yaml(file):
    with open(file, "r") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def reverse_dictionary(d):
    return {v: k for k, v in d.items()}


def delete_directory(directory):
    if os.path.isdir(directory):
        shutil.rmtree(directory)


def make_directory(directory, delete=False, exist_ok=True):
    if delete:
        delete_directory(directory)
    if not os.path.isdir(directory):
        os.makedirs(directory, exist_ok=exist_ok)
    return os.path.abspath(directory)


def files_in_folder(folder):
    return [
        os.path.join(folder, n)
        for n in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, n))
    ]


def folders_in_folder(folder):
    return [
        os.path.join(folder, n)
        for n in os.listdir(folder)
        if os.path.isdir(os.path.join(folder, n))
    ]


def stdout_logger(name):
    """
    Use this logger to standardize log output
    """
    log = logging.getLogger(name)
    log.propagate = False
    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(levelname)-8s %(message)s")
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.DEBUG)
    log.handlers = [stream_handler]
    log.setLevel(logging.DEBUG)
    return log


class class_or_instance_method(classmethod):
    def __get__(self, instance, type_):
        descr_get = super().__get__ if instance is None else self.__func__.__get__
        return descr_get(instance, type_)
