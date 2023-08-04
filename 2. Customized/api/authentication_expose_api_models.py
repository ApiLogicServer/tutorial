from safrs import SAFRSAPI
import safrs
import importlib
import pathlib
import logging as logging

# use absolute path import for easier multi-{app,model,db} support
database = __import__('database')

app_logger = logging.getLogger(__name__)

app_logger.debug("\napi/expose_api_models.py - endpoint for each table")


def expose_models(api, method_decorators = []): 
    """
        Declare API - on existing SAFRSAPI to expose each model - API automation 
        - Including get (filtering, pagination, related data access) 
        - And post/patch/update (including logic enforcement) 

        Invoked at server startup (api_logic_server_run) 

        You typically do not customize this file 
        - See https://apilogicserver.github.io/Docs/Tutorial/#customize-and-debug 
    """
    api.expose_object(database.authentication_models.Category, method_decorators= method_decorators)
    api.expose_object(database.authentication_models.Customer, method_decorators= method_decorators)
    api.expose_object(database.authentication_models.CustomerDemographic, method_decorators= method_decorators)
    api.expose_object(database.authentication_models.Department, method_decorators= method_decorators)
    api.expose_object(database.authentication_models.Employee, method_decorators= method_decorators)
    api.expose_object(database.authentication_models.Union, method_decorators= method_decorators)
    api.expose_object(database.authentication_models.EmployeeAudit, method_decorators= method_decorators)
    api.expose_object(database.authentication_models.EmployeeTerritory, method_decorators= method_decorators)
    api.expose_object(database.authentication_models.Territory, method_decorators= method_decorators)
    api.expose_object(database.authentication_models.Location, method_decorators= method_decorators)
    api.expose_object(database.authentication_models.Order, method_decorators= method_decorators)
    api.expose_object(database.authentication_models.OrderDetail, method_decorators= method_decorators)
    api.expose_object(database.authentication_models.Product, method_decorators= method_decorators)
    api.expose_object(database.authentication_models.Region, method_decorators= method_decorators)
    api.expose_object(database.authentication_models.SampleDBVersion, method_decorators= method_decorators)
    api.expose_object(database.authentication_models.Shipper, method_decorators= method_decorators)
    api.expose_object(database.authentication_models.Supplier, method_decorators= method_decorators)
    return api
