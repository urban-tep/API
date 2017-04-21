
Brockmann Consult Processing centre interfaces
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

    http://www.brockmann-consult.de/bc-wps/wps/calvalus?Service=WPS&Request=GetCapabilities


- WPS getCapabilities response

  Sample response XML can be found in :ref:`GetCapabilitiesResponse`. Important information about the response XML is explained below.

  +---------------------------+--------------------------------------------------------------------------------+
  | Element name              |  Description                                                                   |
  +===========================+================================================================================+
  | wps:ProcessOfferings      | a list of available services.                                                  |
  |                           |                                                                                |
  |                           | *Possible values* :                                                            |
  |                           |                                                                                |
  |                           | - urbantep-subsetting~1.0~Subset                                               |
  |                           | - urbantep-fmask~3.2~Fmask8                                                    |
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

    http://www.brockmann-consult.de/bc-wps/wps/calvalus?Service=WPS&Request=DescribeProcess&Version=1.0.0&Identifier=<service_id>

  Additional information:

  +---------------------------+--------------------------------------------------------------------------------+
  | Parameter me              |  Description                                                                   |
  +===========================+================================================================================+
  | service_id                | the value can be obtained from the :code:`identifier` of the selected service  |
  |                           |                                                                                |
  |                           | in the getCapabilities response. When the value is not known, use :code:`all`. |
  +---------------------------+--------------------------------------------------------------------------------+

- WPS describeProcess response

  Sample response XML for urbantep-subsetting~1.0~Subset service can be found in :ref:`DescribeProcessResponse`. Important information about the response XML is explained below.

  +---------------------------+--------------------------------------------------------------------------------+
  | Element name              |  Description                                                                   |
  +===========================+================================================================================+
  | ProcessDescription        | a list of available services                                                   |
  +---------------------------+--------------------------------------------------------------------------------+
  | wps:Process               | information about a specific service. The :code:`identifier` tag is used in    |
  |                           |                                                                                |
  |                           | the DescribeProcess request to inquire a specific service.                     |
  +---------------------------+--------------------------------------------------------------------------------+
  | wps:processVersion        | the version number of the service                                              |
  +---------------------------+--------------------------------------------------------------------------------+


Processing Execution
^^^^^^^^^^^^^^^^^^^^

This service is used by the portal to send a processing request to the WPS. The request shall be constructed based on the DescribeProcess response of the selected service.

- WPS execute request

  Sample request XML to urbantep-subsetting~1.0~Subset service can be found in :ref:`ExecuteRequest`. Here is information about the parameters in this request:

  +--------------------------+---------------------------------------------------------------------------------+
  | Parameter name           |  Description                                                                    |
  +==========================+=================================================================================+
  | identifier               | the service_id of the processor.                                                |
  |                          |                                                                                 |
  |                          | *Possible values* :                                                             |
  |                          |                                                                                 |
  |                          | - urbantep-subsetting~1.0~Subset                                                |
  |                          | - urbantep-fmask~3.2~Fmask8                                                     |
  +--------------------------+---------------------------------------------------------------------------------+
  | productionName           | a name to identify this request. The value entered here will be used            |
  |                          |                                                                                 |
  |                          | as the result file name. *Sample values* :                                      |
  |                          |                                                                                 |
  |                          | - Milano GUF                                                                    |
  |                          | - TEP Subset                                                                    |
  +--------------------------+---------------------------------------------------------------------------------+
  | inputDataSetName         | the value entered here is based on the option(s) listed in                      |
  |                          |                                                                                 |
  |                          | describeProcess response. *Sample values* :                                     |
  |                          |                                                                                 |
  |                          | - DLR GUF 12m Europe Tiles (Urban TEP)                                          |
  |                          | - LC-CCI GUF 300m Global                                                        |
  +--------------------------+---------------------------------------------------------------------------------+
  | minDate                  | the start date of the time series to process in the format of YYYY-MM-dd.       |
  |                          |                                                                                 |
  | (optional)               | *Sample value* : 2010-01-01                                                     |
  +--------------------------+---------------------------------------------------------------------------------+
  | maxDate                  | the end date of the time series to process in the format of YYYY-MM-dd.         |
  |                          |                                                                                 |
  | (optional)               | *Sample value* : 2016-06-01                                                     |
  +--------------------------+---------------------------------------------------------------------------------+
  | regionWKT                | the spatial range of the processing. There are two formats that are             |
  |                          |                                                                                 |
  |                          | supported: Polygon and Bounding box (refer to describeProcess                   |
  |                          |                                                                                 |
  |                          | response for more information). *Sample values* :                               |
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
  |                          |          <BoundingBoxData xmlns="http://www.opengis.net/ows/1.1">               |
  |                          |              <LowerCorner xmlns="http://www.opengis.net/ows/1.1">               |
  |                          |                  -12.83203125 23.56398712845123                                 |
  |                          |              </LowerCorner>                                                     |
  |                          |              <UpperCorner xmlns="http://www.opengis.net/ows/1.1">               |
  |                          |                  11.953125 31.57853542647338                                    |
  |                          |              </UpperCorner>                                                     |
  |                          |          </BoundingBoxData>                                                     |
  |                          |      </wps:Data>                                                                |
  +--------------------------+---------------------------------------------------------------------------------+
  | spatio                   | optional spatial aggregation rules, as also provided as default in              |
  |                          |                                                                                 |
  | Temporal                 | describeProcess response. *Sample values* :                                     |
  |                          |                                                                                 |
  | Aggregation              | - empty : use defaults                                                          |
  |                          | - false : do not aggregate, deliver tiles/scenes instead                        |
  | Parameters               | - true : aggregate, use defaults for all other parameters                       |
  |                          | - a number : aggregate, result shall have provided spatial resolution in meters |
  |                          | - an XML expression                                                             |
  |                          |   ::                                                                            |
  |                          |                                                                                 |
  |                          |      <spatioTemporalAggregationParameters>                                      |
  |                          |        <aggregate>false</aggregate>                                             |
  |                          |        <spatialResolution>60</spatialResolution>                                |
  |                          |        <spatialRule>NEAREST</spatialRule>                                       |
  |                          |        <temporalRules>FIRST</temporalRules>                                     |
  |                          |        <variables>band_1</variables>                                            |
  |                          |        <validPixelExpression>true</validPixelExpression>                        |
  |                          |      </spatioTemporalAggregationParameters>                                     |
  |                          |                                                                                 |
  |                          | with                                                                            |
  |                          |                                                                                 |
  |                          | - aggregate : whether to compute a mosaic/composite, or to deliver tiles/scenes |
  |                          | - spatialResolution : of the target product in meters, may be same as input     |
  |                          | - spatialRule : one of NEAREST, BINNING                                         |
  |                          | - temporalRules : one of FIRST, MIN_MAX, AVG, ON_MAX_SET(ndvi)                  |
  |                          | - variables : band names to be aggregated (band_1 for GUF, ndvi... for Timescan |
  |                          | - validPixelExpression : SNAP band maths expression, e.g. for cloud screening   |
  +--------------------------+---------------------------------------------------------------------------------+
  | outputFormat             | the desired format of the product. The options are listed in                    |
  |                          |                                                                                 |
  |                          | describeProcess response. *Sample values* :                                     |
  |                          |                                                                                 |
  |                          | - GeoTIFF-BigTIFF                                                               |
  |                          | - NetCDF4                                                                       |
  |                          | - GeoTIFF                                                                       |
  +--------------------------+---------------------------------------------------------------------------------+



- WPS execute response (accepted)

  Sample accepted response XML can be found in :ref:`ExecuteResponseAccepted`. Here is information about the parameters in this response:

  +--------------------------+---------------------------------------------------------------------------------+
  | Element name             |  Description                                                                    |
  +==========================+=================================================================================+
  | wps:ExecuteResponse      | attribute ``statusLocation`` indicates the URL to retrieve the status           |
  |                          |                                                                                 |
  |                          | of the process in GET protocol.                                                 |
  +--------------------------+---------------------------------------------------------------------------------+

- WPS execute response (final)

  Sample final response XML can be found in :ref:`ExecuteResponseFinal`. Here is information about the parameters in this response:

  +--------------------------+---------------------------------------------------------------------------------+
  | Element name             |  Description                                                                    |
  +==========================+=================================================================================+
  | wps:Status               | indicates the time when the product is generated.                               |
  +--------------------------+---------------------------------------------------------------------------------+
  | wps:Output               | each Output element represents a single file of the results. Multiple           |
  |                          |                                                                                 |
  |                          | number of this element is possible. The ``wps:Reference`` attribute             |
  |                          |                                                                                 |
  |                          | indicates the location of the corresponding product.                            |
  +--------------------------+---------------------------------------------------------------------------------+


Result Status & Retrieval
^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two parts of this service: status monitoring and result retrieval.
The status monitoring allows the portal to monitor the status of each requested process. This service is invoked in a defined time interval set by the portal until the process is finished.
The results are available as a HTTP URL and are included as a response of the GetStatus request (after the process has been finished).

- WPS getStatus request

  The URL is generated automatically by the WPS and is available in the asynchronous execute response. Sample getStatus request URL:
  ::

    http://www.brockmann-consult.de/bc-wps/wps/calvalus?Service=WPS&Request=GetStatus&JobId=20160622085915_L2Plus_192611589de0f3


- WPS getStatus response

  Successful processing will return the same response ase the WPS execute response (final). The sample XML is available in :ref:`ExecuteResponseFinal`.


- Download

  The download of the product(s) is via HTTP protocol by following the given link(s) in the final execute response.

- Result metadata

  Each process that produces output(s) comes with result metadata file. The URL to this file is available in the execute response (final). A sample
  metadata file is available in :ref:`ResultMetadataFile`.



