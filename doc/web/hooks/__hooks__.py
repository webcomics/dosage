# -*- coding: iso-8859-1 -*-
import os


def compress_javascript(config, output_path):
    """Minify JS files."""
    from mediacompress import compress_js_files
    compress_js_files(output_path, excludes=("*.min.js",))


def compress_css(config, output_path):
    """Minify CSS files."""
    from mediacompress import compress_css_files
    compress_css_files(output_path)


def chmod(config):
    """Set correct file permissions."""
    output_dir = config["output_dir"]
    for dirpath, dirnames, filenames in os.walk(output_dir):
        for dirname in dirnames:
            os.chmod(os.path.join(dirpath, dirname), 0755)
        for filename in filenames:
            os.chmod(os.path.join(dirpath, filename), 0644)


hooks = {
    'site.output.post': [compress_javascript, compress_css],
    'site.done': [chmod],
}
