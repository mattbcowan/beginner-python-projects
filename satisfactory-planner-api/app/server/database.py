import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "IGNORE"
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
