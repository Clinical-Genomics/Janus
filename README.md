# Janus

In ancient Roman religion and myth, Janus ( JAY-nəs; Latin: Ianvs [ˈi̯aːnʊs]) is the god of beginnings, gates, transitions, time, duality, doorways, passages, frames, and endings. He is usually depicted as having two faces. The month of January is named for Janus (Ianuarius). Janus presided over the beginning and ending of conflict, and hence war and peace. 

## For developers

### Flow overview

Janus can receive post requests that contain a `CollectQCRequest` (see `janus/dto/collect_qc_request.py`).
Using the information within the request Janus fetches and parses files. Janus uses `FileTag` to identify the model in which the data should be parsed, but more importantly the parsing function required to achieve that. Janus then constructs a final model that will contain all the parsed information and send back a `CollectQCResponse`.

### Adding new models and parsing functions to Janus

To add new parsing functionality to Janus:

1. Check if the file tag is represented in `constants/FileTag.py`
2. Check if the parsing functions can parse the metrics file. See in fixtures for currently available structures.
3. Add a model to the `models/<metrics>` that will hold the parsed data.
4. Add or update a model in `modles/workflow`.
5. If a new workflow was added create a function `collect_{workflow}_metrics` in the `CollectQCService`. See existing functions for guidance.
6. If a new workflow was added update the `get_case_info_for_workflow` with the workflow parsing function.
7. Add/Update tests to ensure the parsing can be successful 