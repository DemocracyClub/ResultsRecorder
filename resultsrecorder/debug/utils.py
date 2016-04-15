from django.conf import settings

from scss.compiler import compile_file

from staticfiles_dotd.utils import render

def render_file(filename):
    if filename.endswith('.scss') or filename.endswith('.css'):
        return compile_file(
            filename,
            output_style='legacy' if settings.DEBUG else 'compressed',
        )

    return render(filename)
