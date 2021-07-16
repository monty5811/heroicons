from jinja2 import DictLoader, Environment

from iconic.jinja import iconic_icon


def make_environment(index_template):
    env = Environment(loader=DictLoader({"index": index_template}))
    env.globals.update(
        {
            "iconic_icon": iconic_icon,
        }
    )
    return env


def test_success_simple():
    env = make_environment('{{ iconic_icon("announcement") }}')
    template = env.get_template("index")

    result = template.render()

    assert result.startswith(
        '<svg width="24" height="24" fill="none" viewBox="0 0 24 24" '
        + 'stroke="currentColor">'
    )
    assert "<path" in result
    assert result.endswith("</svg>\n")


def test_success_complete():
    env = make_environment(
        '{{ iconic_icon("announcement", size=48, class="h-4 w-4", '
        + 'data_test="a < 2") }}'
    )
    template = env.get_template("index")

    result = str(template.render())

    assert result.startswith(
        '<svg width="48" height="48" class="h-4 w-4" data-test="a &lt; 2" '
        + 'fill="none" viewBox="0 0 24 24" stroke="currentColor">'
    )
    assert "<path" in result
    assert result.endswith("</svg>\n")
