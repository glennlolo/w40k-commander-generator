import logging

from comgen.comgen import ComGen

logger = logging.getLogger(__name__)

def generate(options):
    """
    Given commanders types specifications, generate their portraits and names

    Args:
        options (collection): Generation options provided

    Returns:
        list: Return a list of `ComGen` object containing all the commanders attributes 
    """

    if options["debug"]:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(message)s', level=logging.INFO)

    com_gen = ComGen(options)

def exportCommanders(commanders, export_type):
    """
    Export the generated commanders to a file in the specified format.

    Args:
        commanders (list): List of generated commanders
        export_type (str): Export format (e.g. "json", "csv")

    Returns:
        None
    """