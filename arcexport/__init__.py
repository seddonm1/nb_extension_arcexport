# file __init__.py
import os
import os.path

from traitlets.config import Config
from nbconvert.exporters.html import HTMLExporter

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


class ArcExporter(HTMLExporter):
    """
    Arc Exporter
    """

    # If this custom exporter should add an entry to the
    # "File -> Download as" menu in the notebook, give it a name here in the
    # `export_from_notebook` class member
    export_from_notebook = "Arc (.json)"

    def _file_extension_default(self):
        """
        The new file extension is `.test_ext`
        """
        return '.test_ext'

    @property
    def template_path(self):
        """
        We want to inherit from HTML template, and have template under
        `./templates/` so append it to the search path. (see next section)
        """
        return super().template_path+[os.path.join(os.path.dirname(__file__), "templates")]

    def _template_file_default(self):
        """
        We want to use the new template we ship with our library.
        """
        return 'test_template'  # full
