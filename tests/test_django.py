import django
from django.conf import settings
from django.template import Context, Template

settings.configure(
    ROOT_URLCONF=__name__,  # Make this module the urlconf
    SECRET_KEY="insecure",
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "APP_DIRS": False,
        },
    ],
    INSTALLED_APPS=["iconic"],
)
urlpatterns = []
django.setup()


def test_success_simple():
    template = Template("{% load iconic %}" + '{% iconic_icon "announcement" %}')

    result = template.render(Context())

    assert result.startswith(
        '<svg width="24" height="24" fill="none" viewBox="0 0 24 24" '
        + 'stroke="currentColor">'
    )
    assert "<path" in result
    assert result.endswith("</svg>\n")


def test_success_complete():
    template = Template(
        "{% load iconic %}"
        + '{% iconic_icon "announcement" size=48 class="h-4 w-4" '
        + 'data_test="a < 2" %}'
    )

    result = template.render(Context())

    assert result.startswith(
        '<svg width="48" height="48" class="h-4 w-4" data-test="a &lt; 2" '
        + 'fill="none" viewBox="0 0 24 24" stroke="currentColor">'
    )
    assert "<path" in result
    assert result.endswith("</svg>\n")
