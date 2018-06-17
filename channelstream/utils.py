from pyramid.renderers import render


def handle_cors(request):
    settings = request.registry.settings
    if not settings["allow_cors"]:
        request.response.headers.add("Access-Control-Allow-Origin", "*")
    else:
        origin = request.headers.get("Origin") or "<>"
        for domain in settings["allow_cors"]:
            if domain in origin:
                request.response.headers.add("Access-Control-Allow-Origin", "*")
                break

    request.response.headers.add("XDomainRequestAllowed", "1")
    request.response.headers.add(
        "Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT"
    )
    request.response.headers.add(
        "Access-Control-Allow-Headers",
        "Content-Type, Depth, User-Agent, "
        "X-File-Size, X-Requested-With, "
        "If-Modified-Since, X-File-Name, "
        "Cache-Control, Pragma, Origin, "
        "Connection, Referer, Cookie",
    )
    request.response.headers.add("Access-Control-Max-Age", "86400")


def swagger_ui_script_template(request, spec_route_name, **kwargs):
    """
    Generates the <script> code that bootstraps Swagger UI, it will be injected
    into index template
    :param request:
    :param swagger_json_route:
    :return:
    """
    return render("templates/explorer.jinja2", value=(), request=request)
