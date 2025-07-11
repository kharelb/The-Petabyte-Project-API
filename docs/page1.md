# TPP MongoDB API

This repository contains an API that allows performing CRUD (Create, Read,
Update, Delete) operations on a MongoDB database specifically designed for the
TPP (The Petabyte Project).

## Features

The API provides the following features:

- **Create**: Insert new documents into the MongoDB database.
- **Read**: Retrieve documents from the database.
- **Update**: Modify existing documents in the database.
- **Delete**: Remove documents from the database.

## Collections and Endpoints
| Collection                                  | Endpoint             |
|---------------------------------------------|----------------------|
| [Data](#dta)                                | /data                |
| [Survey](#survey)                           | /survey              |
| [Candidate Results](#candidate-results)     | /candidate_results   |
| [Processing Outcomes](#processing-outcomes) | /processing_outcomes |
 | [Job Submissions](#job-submissions)         | /job_submissions     |
| [Pipeline Versions](#pipeline-versions)     | /pipeline_versions   |

## Performing CRUD Operations With Python Requests
Click [here](https://pypi.org/project/requests/) for installation method and 
more about requests module.
There are four __methods__ for CRUD operations:
- __post__: inserts data
- __get__: retrieves data
- __patch__: updates data
- __delete__: deletes data

The basic syntax are as follows:
```python
import requests

# IP address and port are:
ipaddress = server_ip_address
port = server_port
"""
!!!!!
NOTE in all code below you will need to insert the address
and port. The pseudocode here is illustrative only.
!!!!
"""

# General
x = requests.method("http://ipaddress:port/endpoint", headers=headers_file)

# If you want to insert documents then provide a json file like this:
x = requests.post("http://ipaddress:port/endpoint", json=dictionary_file, headers=headers_file)

# If you want to retrieve documents:
x = requests.get("http://ipaddress:port/endpoint", headers=headers_file)

```
*Note: You will need to have headers_file for authenticated transactions.
```python
# First create username in the database.
x = requests.post("http://ipaddress:port/sign_up", json={"username":"user",
                                                        "password": "users_password"})
# Print to see if you are successful or username already exists.
print(x.json())

# Now get a token. By default token lasts 30 days but you can change it like below(time is in days).
x = requests.post("http://ipaddress:port/token/?time=365", data={"username":"user",
                                                          "password": "users_password"})
token = x.json()['access_token']

# Save the token somewhere for future references.
```
```python
# Set the headers with your access token.
headers_file = {"Authorization": f"Bearer {token}"}
```

**__For Complete Tutorial Refer to This [Page](page2.md)__

## Schemas For Each Collection
- ### Data
```python
data = {
    'start_date_time': None,                # float MJD (45000-63000)
    'obs_length': None,                     # float seconds (1, 40_000)
    'ra_j': None,                           # float decimal degrees (0, 360)
    'dec_j': None,                          # float decimal degrees (-90, 90)
    'source_name': None,                    # string
    'beam': None,                           # int default to zero if observing system doesn't have beams.
    'regex_filename': None,                 # string without '/'
    'n_files': None,                        # int
    'md5_file': None,                       # List of strings
    'location_on_filesystem': None,         # str
    'survey': None,                         # str maximum of 20 characters
    'size': None                            # int in the units of MB.
}
```
- ### Survey
```python
survey = {
    'survey': None,                         # str
    'parent_survey': None,                  # str limit to 20 characters
    'f_hi': None,                           # float (250 - 40_000)MHz
    'f_low': None,                          # float (250 - 40_000)MHz
    'zap_array': None,                      # Array of integers (0, 32000)
    'sampling_time': None,                  # float (1 - 40_000)microseconds
    'number_of_frequency_channels': None,   # int (10-20_000)
    'backend': None,                        # str Default to 16 characters
    'backend_mode': None,                   # str Default to 16 characters
    'telescope': None,                      # str Default to 16 characters
    'number_of_bits': None,                 # int (1 - 64)
    'no_of_pols': None,                     # int (1 - 4)
    'pol_type': None,                       # str less than 10 characters
    't_sys': None                           # float (0-500) t_sys = t_rec + t_sky    
}
```
- ### Job Submissions
```python
job_submissions = {
    "pipelineID": None,                     # str
    "dataID": None,                         # str
    "started_globus": None,                 # Optional: "YYYY-MM-DDTHH:MM:SS"
    "started_transfer_data": None,          # Optional: "YYYY-MM-DDTHH:MM:SS"
    "started_slurm": None,                  # Optional: "YYYY-MM-DDTHH:MM:SS"
    "status": {
        "completed": None,                  # Optional: True or False
        "date_of_completion": None,         # Optional: "YYYY-MM-DDTHH:MM:SS"
        "error": None                       # Optional: str
    },
    "username": None,                       # Optional: str
    "duration": None,                       # Optional: float in seconds
    "target_directory": None,               # Optional: str
    "log_name": None,                       # Optional: str
    "log_dir": None                         # Optional: str
}
```
- ### Processing Outcomes
```python
processing_outcomes = {
    'submissionID': None,                   # str
    'dataID': None,                         # str
    'node_name': None,                      # Optional : str
    'rfi_fraction': None,                   # Optional : float (0.0 - 1.0)
    'rms_prezap': None,                     # Optional : float
    'rms_postzap': None,                    # Optional : float
    'job_start': None,                      # Optional : "YYYY-MM-DDTHH:MM:SS"
    'job_end': None,                        # Optional : "YYYY-MM-DDTHH:MM:SS"
    'job_state_time': None,                 # Optional : "YYYY-MM-DDTHH:MM:SS"
    'job_state': None,                      # Optional : str (e.g., "Completed", "Failed", etc.)
    'fetch_histogram': None,                # Optional : List of floats
    'n_members': None,                      # Optional : int should be >= 0
    'n_detections': None,                   # Optional : int should be >= 0
    'n_candidates': None,                   # Optional : int should be >= 0
    'working_directory': None,              # Optional : str
    'output_directory': None                # Optional : str
}
```
- ### Candidate Results
```python
candidate_results = {
    "submissionID": None,                   # str
    "outcomeID": None,                      # str
    "dataID": None,                         # str
    "dm": None,                             # Optional: float pc/cm^3
    "tcand": None,                          # Optional: float (45000-62000)MJD
    "fetch_width": None,                    # Optional: float (0-128)ms
    "gl": None                              # Optional: float (0-360) degrees
    "gb": None                              # Optional: float [-90, 90] degrees
    "f_ctr": None                           # Optional: float (200-50000)MHz
    "detected_width": None,                 # Optional: float (0-128)ms
    "sn": None,                             # Optional: float
    "fetch_score": None,                    # Optional: float (0-1)
    "ymw_dm_mw": None,                      # Optional: float
    "ymw_dist": None,                       # Optional: float
    "ymw_z": None,                          # Optional: float
    "ne_dm_mw": None,                       # Optional: float
    "ne_dist": None,                        # Optional: float
    "result_name": None,                    # Optional: str
    "proposed_type": None,                  # Optional: str max 6 characters
    "confirmed_type": None,                 # Optional: str max 6 characters
    "interesting_info": {
        "is_interesting": None,             # Optional: True or False
        "user": None                        # Optional: str max 20 characters
    },
    "periodicity_info": {
        "periodicity_done": None,           # Optional: True or False
        "user": None                        # Optional: str max 20 characters
    },
    "differencing_info": {
        "differencing_done": None,          # Optional: True or False
        "user": None                        # Optional: str max 20 characters
    },
    "inspection_info": {
     "was_inspected": None,                 # Optional: True or False
     "user": str                            # Optional: str max 20 characters
    },
    "note_info": {
        "note": None,                       # Optional: str max 200 characters
        "when_submitted": None,              # Optional: "YYYY-MM-DDTHH:MM:SS"
        "user": str                          # Optional: str max 20 characters
    }
}
```
- ### Pipeline Versions
```python
pipeline_versions = {
    'launcher_version': None,               # str
    'pipeline_version': None,               # str
    'heimdall_version': None,               # str
    'your_version': None,                   # str
    'candcsvmaker_version': None,           # str
    'decimate_version': None,               # str
    'ddplan_version': None                  # str
}
```
[__Home Page__](README.md) | [__Next Page__](page2.md)
