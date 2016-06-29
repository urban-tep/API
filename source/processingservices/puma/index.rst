
PUMA Provider
=============

.. toctree::
   :maxdepth: 2

Services Discovery
^^^^^^^^^^^^^^^^^^

GET /integration/services

Expected header:
 Content-Type: application/json; charset=utf-8
 
Response (success):
HTTP 200
 [{
   "id": "gufAnalysis",
   "description": "Combine Global Urban Footprint with Population data"
 }, {
   "id": "gsiAnalysis",
   "description": "Combine Global Settlements Inventory with Population data"
 }]

The response contains ids and descriptions of available process in an array.

This one is not yet implemented.

Service Description
^^^^^^^^^^^^^^^^^^^

GET /integration/services/{idOfService}

Expected header:
 Content-Type: application/json; charset=utf-8
 
Response (success):
HTTP 200
 {
    "parameters": {
      "url": {
         "required": true,
         "type": "URL"
      }
   }
   "method": "POST",
   "execution": "/integration/process"
 }
 
If the query succeeds, it returns the execution endpoint together with method and parameters. Every parameter contains information about whether it is required and what type is expected. 

 Response (error):
 HTTP 404
 {
   "message": "Process with given id doesn't exist"
 }

This methos isn't implemented yet

Processing Execution
^^^^^^^^^^^^^^^^^^^^

POST /integration/process

Expected payload:
 {
   "url": "{UrlOfTheGeotiffToProcess}"
 }
Expected header:
 Content-Type: application/json; charset=utf-8

Response (success):
HTTP 200
 {
   "id": "Uuid"
 }

Response (error):
HTTP 400
 {
   "message": "error message"
 }

The portal will use this endpoint to initiate the import. PUMA will return an unique identifier for Endpoint 2.
PUMA downloads the specified file, prepares it for the platform, saves, connects it to predefined metadata and runs appropriate analyses and generates url to view it in PUMA. Once everything is done, the url is available from endpoint 2.

Result Retrieval
^^^^^^^^^^^^^^^^

GET /integration/status?id={Uuid}

Response (process finished):
HTTP 200
 {
   "status": "Finished",
   "sourceUrl": "{UrlOfTheGeotiffToProcess}",
   "url": "{UrlToTheDataInPUMA}"
 }

Response (process underway - downloading file):
HTTP 200
 {
   "status": "Started",
   "sourceUrl": "{UrlOfTheGeotiffToProcess}",
   "message": "{status message}"
 }

Response (process underway - processing file):
HTTP 200
 {
   "status": "Processing",
   "sourceUrl": "{UrlOfTheGeotiffToProcess}",
   "message": "{status message}"
 }

Response (process failed):
HTTP 200
 {
   "status": "Error",
   "sourceUrl": "{UrlOfTheGeotiffToProcess}",
   "message": "{error message}"
 }

Response (request error):
HTTP 400
 {
   "message": "{error message}"
 }

The portal will use this endpoint to check the status of processing in PUMA, using the identifier obtained from endpoint 1. Once the processing is finished, the portal will receive url to the data in PUMA and it will redirect the user to it / display PUMA using the url / display link to the url.
