# openapi-parse-min
The plugin for openAPI is great for tracking the flow of an application and to identify where data is going. The problem is that it produces too much information and can be difficult to sift through for relevant data in the JSON output. What openapi-parse-min does it make it so that we can get necessary data exported to screen and a .txt file for adding to architecture diagrams.

We are parsing the following for each api call discovered by openAPI

- Host
- Path
- Method

## Instructions

1. `git clone https://github.com/d1s4rm/openapi-parse-min`
2. `cd openapi-parse-min`
3. `python3 openapi-parse-min.py <path-to-file-name>`
