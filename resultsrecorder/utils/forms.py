from django.contrib import messages

def emit_errors(request, form):
    for field, errors in form.errors.items():
        for x in errors:
            prefix = '%s: ' % field if field != '__all__' else ''
            messages.error(request, "%s%s" % (prefix, x))
