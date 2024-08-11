from typing import Any

import requests
from jinja2 import Environment, PackageLoader, select_autoescape


def openapi_type_to_python_type(openapi_type: str) -> str:
    if openapi_type == "integer":
        return "int"
    if openapi_type == "string":
        return "str"
    if openapi_type == "boolean":
        return "bool"
    raise Exception("Unknown type")


def parse_endpoints_by_tag(openapi: Any):
    tags = dict()
    for path, endpoints in openapi["paths"].items():
        operation_id = endpoints["get"]["operationId"]
        function_name = "_".join(operation_id.split("_")[1:])
        params = []
        tag = endpoints["get"]["tags"][0]

        for param in endpoints["get"]["parameters"]:
            name = param["name"]
            if name == "token":
                continue

            type = None
            transform = None

            if "type" in param["schema"]:
                type = openapi_type_to_python_type(param["schema"]["type"])

                if "retype" in param["schema"]:  # noqa: SIM102
                    if param["schema"]["retype"] == "semicolon-separated-string-to-list":
                        type = "Sequence[str]"
                        transform = "join_with_semicolon"

            # Handle enums
            elif "allOf" in param["schema"]:
                assert len(param["schema"]["allOf"]) == 1
                assert "$ref" in param["schema"]["allOf"][0]
                ref = param["schema"]["allOf"][0]["$ref"]
                ref_name = ref.split("/")[-1]
                type = f"Literal{openapi['components']['schemas'][ref_name]['enum']}"
            else:
                raise Exception("Unknown param type")

            params.append(
                {
                    "required": param["required"],
                    "param": name,
                    "name": param["schema"].get("rename") or name,
                    "type": type,
                    "transform": transform,
                }
            )

        if tag not in tags:
            tags[tag] = []

        tags[tag].append(
            {
                "function_name": function_name,
                "path": path,
                "params": params,
                "return_top_level_data": operation_id
                in ["tiktok_user_posts_from_username", "tiktok_user_posts_from_secuid"],
            }
        )

    return tags


def main():
    openapi = requests.get("https://ensembledata.com/apis/openapi.json").json()

    env = Environment(
        loader=PackageLoader("codegen"),
        autoescape=select_autoescape(),
        lstrip_blocks=True,
        trim_blocks=True,
    )

    tags = parse_endpoints_by_tag(openapi)
    client_template = env.get_template("client.jinja")

    client_content = client_template.render(tags=tags, async_methods=False)
    async_client_content = client_template.render(tags=tags, async_methods=True)

    with open("ensembledata/api/_client.py", "w") as file:
        file.write(client_content)

    with open("ensembledata/api/_async_client.py", "w") as file:
        file.write(async_client_content)


if __name__ == "__main__":
    main()
