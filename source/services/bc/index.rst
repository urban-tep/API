
Brockmann Consult Provider
==========================

.. toctree::
   :maxdepth: 2

Services Discovery
^^^^^^^^^^^^^^^^^^

- WPS getCapabilities request

  Sample getCapabilities request URL:
  ::
    http://www.brockmann-consult.de/bc-wps/wps/calvalus?Service=WPS&Request=GetCapabilities


- WPS getCapabilities response

  Sample response XML can be found in :ref:`GetCapabilitiesResponse`. Important information about the response XML is explained below.

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

- WPS execute request

  Sample request XML to urbantep-subsetting~1.0~Subset service can be found in :ref:`ExecuteRequest`. Here is information about the parameters in this request:

  +--------------------------+---------------------------------------------------------------------------------+
  | Parameter name           |  Description                                                                    |
  +==========================+=================================================================================+
  | productionName           | a name to identify this request. The value entered here will be used            |
  |                          |                                                                                 |
  |                          | as the result file name.                                                        |
  +--------------------------+---------------------------------------------------------------------------------+
  | inputDataSetName         | the value entered here is based on the option(s) listed in                      |
  |                          |                                                                                 |
  |                          | describeProcess response.                                                       |
  +--------------------------+---------------------------------------------------------------------------------+
  | regionWKT                | the spatial range of the processing. There are two formats that are             |
  |                          |                                                                                 |
  |                          | supported: Polygon and Bounding box (refer to describeProcess                   |
  |                          |                                                                                 |
  |                          | response for more information).                                                 |
  +--------------------------+---------------------------------------------------------------------------------+
  | calvalus.l3.parameters   | calvalus-specific parameters for L3 processing. When required,                  |
  |                          |                                                                                 |
  |                          | it will be indicated in describeProcess response and with a sample              |
  |                          |                                                                                 |
  |                          | values.                                                                         |
  +--------------------------+---------------------------------------------------------------------------------+
  | outputFormat             | the desired format of the product. The options are listed in                    |
  |                          |                                                                                 |
  |                          | describeProcess response.                                                       |
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


Result Retrieval
^^^^^^^^^^^^^^^^

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



