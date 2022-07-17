from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_resource,
    delete_resource,
    retrieve_resource,
    retrieve_resources,
    update_resource,
)

from app.server.models.resource import (
    ErrorResponseModel,
    ResponseModel,
    ResourceSchema,
    UpdateResourceModel,
)

router = APIRouter()


@router.post("/", response_description="Resource data added to the database")
async def add_resource_data(resource: ResourceSchema = Body(...)):
    resource = jsonable_encoder(resource)
    new_resource = await add_resource(resource)
    return ResponseModel(new_resource, "Resource added successfully.")


@router.get("/", response_description="Retrieved all resources")
async def get_resources():
    resources = await retrieve_resources()
    if resources:
        return ResponseModel(resources, "Resources data retrieved successfully.")
    return ResponseModel(resources, "Empty list returned")


@router.get("/{id}", response_description="Resource data retrieved")
async def get_resource_data(id):
    resource = await retrieve_resource(id)
    if resource:
        return ResponseModel(resource, "Resource data retrieved successfully.")
    return ErrorResponseModel("An error occurred.", 404, "Resource doesn't exist.")


@router.put("/{id}")
async def update_resource_data(id: str, req: UpdateResourceModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_resource = await update_resource(id, req)
    if updated_resource:
        return ResponseModel(
            "Resource with ID: {} name update is successful".format(id),
            "Resource name was updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred", 404, "There was an error updating the resource data."
    )


@router.delete(
    "/{id}", response_description="Resource data was deleted from the database"
)
async def delete_resource_data(id: str):
    deleted_resource = await delete_resource(id)
    if deleted_resource:
        return ResponseModel(
            "Resource with ID: {} removed".format(id), "Resource delete successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Resource with id {0} doesn't exist".format(id)
    )
