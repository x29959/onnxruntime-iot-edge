# download model
import json
from azureml.core import Workspace, Model, VERSION
from azureml.core.authentication import ServicePrincipalAuthentication

print(VERSION)

with open("config.json", "r") as f:
    config = json.load(f)

auth = ServicePrincipalAuthentication(
    config["tenant_id"],
    config["service_principal_id"],
    config["service_principal_password"]
)

ws = Workspace.create(
    name=config["workspace_name"],
    auth=auth,
    subscription_id=config['subscription_id'],
    resource_group=config['resource_group'],
    exist_ok=True,
    show_output=True,
)

model = Model(ws, name="TinyYOLO")

model.download(target_dir="modules/InferenceModule/")
