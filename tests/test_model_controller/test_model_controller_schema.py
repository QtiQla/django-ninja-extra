from ninja_extra import NinjaExtraAPI

from .samples import (
    EventModelControllerAutoGeneratedSchema,
    EventModelControllerDifferentPagination,
    EventModelControllerRetrieveAndList,
    EventModelControllerWithDefinedSchema,
)


def test_event_model_open_api_schema_case_3():
    api = NinjaExtraAPI()
    api.register_controllers(EventModelControllerDifferentPagination)
    schema = api.get_openapi_schema()

    assert "get" in schema["paths"]["/api/event-case-3/"]

    assert "post" not in schema["paths"]["/api/event-case-3/"]
    assert schema["paths"]["/api/event-case-3/"]["get"]["parameters"] == [
        {
            "in": "query",
            "name": "limit",
            "schema": {
                "default": 100,
                "minimum": 1,
                "title": "Limit",
                "type": "integer",
            },
            "required": False,
        },
        {
            "in": "query",
            "name": "offset",
            "schema": {
                "default": 0,
                "minimum": 0,
                "title": "Offset",
                "type": "integer",
            },
            "required": False,
        },
    ]
    assert list(schema["components"]["schemas"].keys()) == [
        "Input",
        "EventSchema",
        "NinjaPaginationResponseSchema_EventSchema_",
    ]


def test_event_model_open_api_schema_case_2():
    api = NinjaExtraAPI()
    api.register_controllers(EventModelControllerWithDefinedSchema)

    schema = api.get_openapi_schema()
    assert "post" in schema["paths"]["/api/event-case-2/"]
    assert "get" in schema["paths"]["/api/event-case-2/"]

    assert "get" in schema["paths"]["/api/event-case-2/{id}"]
    assert "put" in schema["paths"]["/api/event-case-2/{id}"]
    assert "delete" in schema["paths"]["/api/event-case-2/{id}"]
    assert "patch" in schema["paths"]["/api/event-case-2/{id}"]

    assert (
        schema["paths"]["/api/event-case-2/"]["get"]["parameters"] == []
    )  # turned off pagination for case-2
    schemas_key = list(schema["components"]["schemas"].keys())

    for item in [
        "EventSchema",
        "CreateEventSchema",
    ]:
        assert item in schemas_key


def test_event_model_open_api_schema_case_4():
    api = NinjaExtraAPI()
    api.register_controllers(EventModelControllerRetrieveAndList)

    schema = api.get_openapi_schema()

    assert "get" in schema["paths"]["/api/event-case-4/"]
    assert "post" not in schema["paths"]["/api/event-case-4/"]

    assert "get" in schema["paths"]["/api/event-case-4/{id}"]
    assert "put" not in schema["paths"]["/api/event-case-4/{id}"]
    assert "delete" not in schema["paths"]["/api/event-case-4/{id}"]
    assert "patch" not in schema["paths"]["/api/event-case-4/{id}"]

    assert schema["paths"]["/api/event-case-4/"]["get"]["parameters"] == [
        {
            "in": "query",
            "name": "page",
            "schema": {
                "title": "Page",
                "default": 1,
                "exclusiveMinimum": 0,
                "type": "integer",
            },
            "required": False,
        },
        {
            "in": "query",
            "name": "page_size",
            "schema": {
                "title": "Page Size",
                "default": 100,
                "exclusiveMaximum": 200,
                "type": "integer",
            },
            "required": False,
        },
    ]
    schemas_key = list(schema["components"]["schemas"].keys())

    for item in [
        "EventSchema",
        "PaginatedResponseSchema_EventSchema_",
    ]:
        assert item in schemas_key


def test_event_model_open_api_auto_gen_schema():
    api = NinjaExtraAPI()
    api.register_controllers(EventModelControllerAutoGeneratedSchema)

    schema = api.get_openapi_schema()
    assert "post" in schema["paths"]["/api/event/"]
    assert "get" in schema["paths"]["/api/event/"]

    assert "get" in schema["paths"]["/api/event/{id}"]
    assert "put" in schema["paths"]["/api/event/{id}"]
    assert "delete" in schema["paths"]["/api/event/{id}"]
    assert "patch" in schema["paths"]["/api/event/{id}"]
    assert schema["paths"]["/api/event/"]["get"]["parameters"] == [
        {
            "in": "query",
            "name": "page",
            "schema": {
                "default": 1,
                "exclusiveMinimum": 0,
                "title": "Page",
                "type": "integer",
            },
            "required": False,
        },
        {
            "in": "query",
            "name": "page_size",
            "schema": {
                "default": 100,
                "exclusiveMaximum": 200,
                "title": "Page Size",
                "type": "integer",
            },
            "required": False,
        },
    ]

    schemas_key = list(schema["components"]["schemas"].keys())

    for item in [
        "EventSchema",
        "EventCreateSchema",
        "PaginatedResponseSchema_EventSchema_",
        "EventPatchSchema",
    ]:
        assert item in schemas_key
    # TODO - fix pathModel in schema for django ninja v1.0rc0
    # assert schema["components"]["schemas"] == {
    #     "EventSchema": {
    #         "properties": {
    #             "id": {"description": "", "title": "Id", "type": "integer"},
    #             "title": {
    #                 "description": "",
    #                 "maxLength": 100,
    #                 "title": "Title",
    #                 "type": "string",
    #             },
    #             "category": {
    #                 "anyOf": [{"type": "integer"}, {"type": "null"}],
    #                 "description": "",
    #                 "title": "Category",
    #             },
    #             "start_date": {
    #                 "description": "",
    #                 "format": "date",
    #                 "title": "Start Date",
    #                 "type": "string",
    #             },
    #             "end_date": {
    #                 "description": "",
    #                 "format": "date",
    #                 "title": "End Date",
    #                 "type": "string",
    #             },
    #         },
    #         "required": ["id", "title", "start_date", "end_date"],
    #         "title": "EventSchema",
    #         "type": "object",
    #     },
    #     "EventCreateSchema": {
    #         "properties": {
    #             "title": {
    #                 "description": "",
    #                 "maxLength": 100,
    #                 "title": "Title",
    #                 "type": "string",
    #             },
    #             "start_date": {
    #                 "description": "",
    #                 "format": "date",
    #                 "title": "Start Date",
    #                 "type": "string",
    #             },
    #             "end_date": {
    #                 "description": "",
    #                 "format": "date",
    #                 "title": "End Date",
    #                 "type": "string",
    #             },
    #         },
    #         "required": ["title", "start_date", "end_date"],
    #         "title": "EventCreateSchema",
    #         "type": "object",
    #     },
    #     "PaginatedResponseSchema_EventSchema_": {
    #         "properties": {
    #             "count": {"title": "Count", "type": "integer"},
    #             "next": {
    #                 "anyOf": [{"type": "string"}, {"type": "null"}],
    #                 "title": "Next",
    #             },
    #             "previous": {
    #                 "anyOf": [{"type": "string"}, {"type": "null"}],
    #                 "title": "Previous",
    #             },
    #             "results": {
    #                 "items": {"$ref": "#/components/schemas/EventSchema"},
    #                 "title": "Results",
    #                 "type": "array",
    #             },
    #         },
    #         "required": ["count", "next", "previous", "results"],
    #         "title": "PaginatedResponseSchema[EventSchema]",
    #         "type": "object",
    #     },
    #     "EventPatchSchema": {
    #         "properties": {
    #             "title": {
    #                 "anyOf": [{"type": "string"}, {"type": "null"}],
    #                 "description": "",
    #                 "title": "Title",
    #             },
    #             "start_date": {
    #                 "anyOf": [{"format": "date", "type": "string"}, {"type": "null"}],
    #                 "description": "",
    #                 "title": "Start Date",
    #             },
    #             "end_date": {
    #                 "anyOf": [{"format": "date", "type": "string"}, {"type": "null"}],
    #                 "description": "",
    #                 "title": "End Date",
    #             },
    #         },
    #         "title": "EventPatchSchema",
    #         "type": "object",
    #     },
    # }
