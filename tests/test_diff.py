import copy

from populi_docs.diff import diff_catalogs, format_changes, headline


def catalog():
    return {
        "models": [
            {
                "name": "Person",
                "slug": "people",
                "objects": [
                    {
                        "name": "Person",
                        "fields": [{"name": "id", "required": True, "type": "int"}],
                    }
                ],
                "actions": [
                    {
                        "name": "index",
                        "method": "GET",
                        "path": "/people",
                        "description": "Retrieves all Person objects.",
                        "params": [{"name": "page", "required": False, "type": "int"}],
                        "filters": [{"name": "first_name", "type": "text"}],
                        "action_params": [],
                        "expands": ["tags"],
                        "permissions": {"note": "", "roles": ["Registrar"]},
                    }
                ],
            }
        ],
        "webhook_events": [{"event": "person_created", "title": "Person Added"}],
    }


def test_identical_catalogs_have_no_changes():
    assert diff_catalogs(catalog(), catalog()) == {}
    assert headline({}) == "no structural changes"


def test_every_kind_of_change_is_reported():
    old, new = catalog(), catalog()
    person = new["models"][0]
    person["objects"][0]["fields"].append({"name": "deleted_at", "type": "datetime"})
    index = person["actions"][0]
    index["filters"].append({"name": "deleted_at", "type": "datetime"})
    index["filters"][0]["type"] = "string"
    index["params"] = []
    index["expands"] = ["tags", "roles"]
    index["permissions"]["roles"] = ["Registrar", "Staff"]
    index["description"] = "Retrieves Person objects."
    extra = copy.deepcopy(index)
    extra.update(name="deleted", path="/people/deleted")
    person["actions"].append(extra)
    new["models"].append(
        {"name": "LtiTool", "slug": "ltitools", "objects": [], "actions": []}
    )
    new["webhook_events"] = [{"event": "person_updated", "title": "Person Updated"}]

    changes = diff_catalogs(old, new)
    assert changes["Models"] == ["+ LtiTool (`ltitools`)"]
    assert changes["Endpoints"] == ["+ `GET /people/deleted` (Person deleted)"]
    assert changes["Object fields"] == ["+ Person.`deleted_at` (datetime)"]
    assert changes["Parameters"] == ["− `GET /people`: parameter `page`"]
    assert changes["Filter conditions"] == [
        "+ `GET /people`: filter `deleted_at` (datetime)",
        "~ `GET /people`: filter `first_name` type 'text' → 'string'",
    ]
    assert changes["Expands"] == ["+ `GET /people`: `roles`"]
    assert changes["Permissions"] == ["~ `GET /people`: Registrar → Registrar, Staff"]
    assert changes["Descriptions"] == ["~ `GET /people`"]
    assert changes["Webhook events"] == [
        "+ `person_updated` (Person Updated)",
        "− `person_created`",
    ]
    assert headline(changes).startswith("models +1; endpoints +1; object fields +1")
    assert "### Filter conditions" in format_changes(changes)


def test_examples_are_not_compared():
    old, new = catalog(), catalog()
    new["models"][0]["actions"][0]["example_response"] = '{"id": "random"}'
    assert diff_catalogs(old, new) == {}
