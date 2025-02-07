## For developers

### Flow overview

Janus can receive post requests that contain a `CollectQCRequest` (see `janus/dto/collect_qc_request.py`).
Using the information within the request Janus fetches and parses files. Janus uses `FileTag` to identify the model in which the data should be parsed, but more importantly the parsing function required to achieve that. Janus then constructs a final model that will contain all the parsed information and send back a `CollectQCResponse`.

### Adding new models and parsing functions to Janus

To add new parsing functionality to Janus:

1. Check if the file tag is represented in `constants/FileTag.py`.
2. Check if the parsing functions can parse the metrics file. See in fixtures for currently available structures.
3. Add a model to the `models/<metrics>` that will hold the parsed data if it is not already present. 
4. Add new or update an existing workflow model in `models/workflow`.
5. If there is a new workflow create a WorkflowCollectQCService in `services/workflow_collect_qc_service.py` that will handle the parsing of the workflow. This Service has to expose a `get_case_info()` function that takes a `CollectQCRequest` and returns a Workflow model.
6. Add the workflow and workflow-service combination to the `workflow_to_service` map.
7. Add/Update tests to ensure the parsing can be successful.