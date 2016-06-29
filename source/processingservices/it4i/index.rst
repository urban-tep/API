
IT4I Processing centre interfaces
==============================================

.. toctree::
   :maxdepth: 2

Services Discovery
^^^^^^^^^^^^^^^^^^

This service is available for the portal to discover all the available services on the WPS. GetCapabilities call of `OGC WPS 1.0 <http://www.opengeospatial.org/standards/wps>`_ standard is used for this service.
This service is invoked so that the portal has the information about services available for the users to use.

- WPS getCapabilities request

  Sample getCapabilities request URL:
  ::

    http://utep.it4i.cz/geoserver/ows?service=WPS&version=1.0.0&request=GetCapabilities


- WPS getCapabilities response

  Sample response XML can be found in :ref:`IT4IGetCapabilitiesResponse`. Important information about the response XML is explained below.

  +---------------------------+--------------------------------------------------------------------------------+
  | Element name              |  Description                                                                   |
  +===========================+================================================================================+
  | wps:ProcessOfferings      | a list of available services                                                   |
  +---------------------------+--------------------------------------------------------------------------------+
  | wps:Process               | information about a specific service. The :code:`identifier` tag is used in    |
  |                           |                                                                                |
  |                           | the DescribeProcess request to inquire a specific service.                     |
  +---------------------------+--------------------------------------------------------------------------------+
  | wps:processVersion        | the version number of the service                                              |
  +---------------------------+--------------------------------------------------------------------------------+


Service Description
^^^^^^^^^^^^^^^^^^^

This service is used by the portal to inquire information about the available parameters of the services.
The inquiry can be specific to a service or multiple services (defined by the *service_id*), or all the available services in the WPS.
This service is invoked when the user has selected a particular service for a processing. The information that is returned as part of the DescribeProcess response
is then displayed on the portal page in the format of a Form, for the users to fill in.

- WPS describeProcess request

  Sample describeProcess request URL:
  ::

    http://utep.it4i.cz/geoserver/ows?service=WPS&version=1.0.0&request=DescribeProcess&identifier=<service_id>

  Additional information:

  +---------------------------+--------------------------------------------------------------------------------+
  | Parameter me              |  Description                                                                   |
  +===========================+================================================================================+
  | service_id                | the value can be obtained from the :code:`identifier` of the selected service  |
  |                           |                                                                                |
  |                           | in the getCapabilities response. When the value is not known, use :code:`all`. |
  +---------------------------+--------------------------------------------------------------------------------+


- WPS describeProcess response

  Sample response XML for Urban-TEP Temporal statistics service can be found in :ref:`IT4IDescribeProcessResponse`. Important elements in the response XML is explained below:

  +---------------------------+--------------------------------------------------------------------------------+
  | Element name              |  Description                                                                   |
  +===========================+================================================================================+
  | ProcessDescription        | a list of available services                                                   |
  +---------------------------+--------------------------------------------------------------------------------+
  | DataInputs                | information about inputs for a specific service along with their data types    |
  |                           |                                                                                |
  |                           | and limitations                                                                |
  +---------------------------+--------------------------------------------------------------------------------+
  | ProcessOutputs            | information about service outputs/results                                      |
  +---------------------------+--------------------------------------------------------------------------------+


Processing Execution
^^^^^^^^^^^^^^^^^^^^

This service is used by the portal to send a processing request to the WPS. The request shall be constructed based on the DescribeProcess response of the selected service.

- WPS execute request

  Sample execute POST request URL:
  ::

    http://utep.it4i.cz/geoserver/ows?service=WPS&version=1.0.0&request=execute&identifier=gs:TemporalStatistics

  The payload of the execute POST request is an XML and an example of this payload for the Urban-TEP Temporal statistics service can be found in :ref:`IT4IExecuteRequest`. Here is information about the input parameters in this request:

  +--------------------------+---------------------------------------------------------------------------------+
  | Parameter name           |  Description                                                                    |
  +==========================+=================================================================================+
  | productionName           | a name to identify this request.                                                |
  +--------------------------+---------------------------------------------------------------------------------+
  | maxCloudCover            | the maximum acceptable cloud cover per input image, floating point number 0-100 |
  +--------------------------+---------------------------------------------------------------------------------+
  | inputDataSet             | the input dataset required for the processing,                                  |
  |                          |                                                                                 |
  |                          | enumeration with the following supported values:                                |
  |                          |                                                                                 |
  |                          |   Landsat_5_7_and_8_Level_1                                                     |
  |                          |                                                                                 |
  |                          |   Landsat_5_Level_1                                                             |
  |                          |                                                                                 |
  |                          |   Landsat_5_Level_1_including_ESA                                               |
  |                          |                                                                                 |
  |                          |   Landsat_7_Level_1                                                             |
  |                          |                                                                                 |
  |                          |   Landsat_7_Level_1_including_ESA                                               |
  |                          |                                                                                 |
  |                          |   Landsat_7_Level_1_including_SLC_off                                           |
  |                          |                                                                                 |
  |                          |   Landsat_7_Level_1_including_SLC_off_and_ESA                                   |
  |                          |                                                                                 |
  |                          |   Landsat_8_Level_1                                                             |
  |                          |                                                                                 |
  |                          |   Landsat_5_7_and_8_Level_1_including_ESA                                       |
  |                          |                                                                                 |
  |                          |   Landsat_5_7_and_8_Level_1_including_SLC_off                                   |
  |                          |                                                                                 |
  |                          |   Landsat_5_7_and_8_Level_1_including_SLC_off_and_ESA                           |
  +--------------------------+---------------------------------------------------------------------------------+
  | minDate                  | the desired start date of the products in the format YYYY-MM-DD                 |
  +--------------------------+---------------------------------------------------------------------------------+
  | maxDate                  | the desired end date of the products in the format YYYY-MM-DD                   |
  +--------------------------+---------------------------------------------------------------------------------+
  | regionWKT / regionBB     | the spatial range of the processing. There are two formats that are             |
  |                          |                                                                                 |
  |                          | supported: Polygon and Bounding box (refer to describeProcess                   |
  |                          |                                                                                 |
  |                          | response for more information). *Sample value* :                                |
  |                          |                                                                                 |
  |                          | - Polygon                                                                       |
  |                          |   ::                                                                            |
  |                          |                                                                                 |
  |                          |      <wps:LiteralData>                                                          |
  |                          |          POLYGON((100 -10,100 0,110 0,110 -10,100 -10))                         |
  |                          |      </wps:LiteralData>                                                         |
  |                          | - Bounding Box                                                                  |
  |                          |   ::                                                                            |
  |                          |                                                                                 |
  |                          |      <wps:Data>                                                                 |
  |                          |        <wps:BoundingBoxData crs="EPSG:4326" dimensions="2">                     |
  |                          |          <ows:LowerCorner>-96.7614750516692 35.4407632348574</ows:LowerCorner>  |
  |                          |          <ows:UpperCorner>-96.6808577826219 35.5328972566257</ows:UpperCorner>  |
  |                          |        </wps:BoundingBoxData>                                                   |
  |                          |      </wps:Data>                                                                |
  +--------------------------+---------------------------------------------------------------------------------+

	The wps:ResponseDocument XML element has to include the attributes storeExecuteResponse="true" status="true" to ensure asynchronous execution of the service and storing/providing the current status during service execution.

- WPS execute response (accepted)

  Sample accepted response XML can be found in :ref:`IT4IExecuteResponseAccepted`. Here is information about the elements in this response:

  +--------------------------+---------------------------------------------------------------------------------+
  | Element name             |  Description                                                                    |
  +==========================+=================================================================================+
  | wps:ExecuteResponse      | attribute ``statusLocation`` indicates the URL to retrieve the status           |
  |                          |                                                                                 |
  |                          | of the process using HTTP GET method.                                           |
  +--------------------------+---------------------------------------------------------------------------------+



Result Status & Retrieval
^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two parts of this service: status monitoring and result retrieval.
The status monitoring allows the portal to monitor the status of each requested process. This service is invoked in a defined time interval set by the portal until the process is finished.

- WPS GetExecutionStatus request

  The URL is generated automatically by the WPS and is available in the asynchronous execute response. Sample getStatus request URL:
  ::

    http://utep.it4i.cz:80/geoserver/ows?service=WPS&version=1.0.0&request=GetExecutionStatus&executionId=8c073e4a-55b4-459b-8175-f6ec64979ee8


- WPS GetExecutionStatus response (running)

  During the execution of the service, the GetExecutionStatus request returns the information about the current status of the ongoing execution. Sample status response XML can be found in :ref:`IT4IExecuteResponseStatus`. Here is information about the interesting elements and attributes in this response:

  +--------------------------+---------------------------------------------------------------------------------+
  | Element name             |  Description                                                                    |
  +==========================+=================================================================================+
  | wps:Status               | contains the information about the current status of service execution          |
  +--------------------------+---------------------------------------------------------------------------------+
  | wps:ProcessStarted       | contains estimated percentage of the service progress                           |
  |                          |                                                                                 |
  | percentCompleted         |                                                                                 |
  +--------------------------+---------------------------------------------------------------------------------+


- WPS GetExecutionStatus response (final)

  After the execution service is completed, the GetExecutionStatus request returns the final response that contains the service results. Sample final response XML can be found in :ref:`IT4IExecuteResponseFinal`. Here is information about the interesting elements in this response:

  +--------------------------+---------------------------------------------------------------------------------+
  | Element name             |  Description                                                                    |
  +==========================+=================================================================================+
  | wps:Status               | indicates the time when the product was generated.                              |
  +--------------------------+---------------------------------------------------------------------------------+
  | wps:Output               | contains the URL to the service product to be retreived using HTTP GET method   |
  +--------------------------+---------------------------------------------------------------------------------+


- Download

  The download of the product(s) is via HTTP protocol by following the given link(s) in the final execute response.

- Result metadata

  The URL to the metadata file will be available in the execute response (final) as another output in the next version of the service. The metadata file will be created based on the sample in :ref:`ResultMetadataFile`.

