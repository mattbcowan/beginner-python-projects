import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config("MONGO_DETAILS")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.satisfactory_planner
resource_collection = database.get_collection("resources")

# Helper Functions
def resource_helper(resource) -> dict:
    return {
        "id": str(resource["_id"]),
        "name": resource["name"],
        "description": resource["description"],
        "stack_size": resource["stack_size"],
    }


# Retrieve all resources from database
async def retrieve_resources():
    resources = []
    async for resource in resource_collection.find():
        resources.append(resource_helper(resource))
    return resources


# Add a resource to the database
async def add_resource(resource_data: dict) -> dict:
    resource = await resource_collection.insert_one(resource_data)
    new_resource = await resource_collection.find_one({"_id": resource.inserted_id})
    return resource_helper(new_resource)


# Retrieve a resource with a matching ID
async def retrieve_resource(id: str) -> dict:
    resource = await resource_collection.find_one({"_id": ObjectId(id)})
    if resource:
        return resource_helper(resource)


# Update a resource with matching ID
async def update_resource(id: str, data: dict):
    # Return false if request body is empty
    if len(data) < 1:
        return False

    resource = await resource_collection.find_one({"_id": ObjectId(id)})

    if resource:
        updated_resource = await resource_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )

        if updated_resource:
            return True
        return False


# Delete a resource from the database
async def delete_resource(id: str):
    resource = await resource_collection.find_one({"_id": ObjectId(id)})
    if resource:
        await resource_collection.delete_one({"_id": ObjectId(id)})
        return True
