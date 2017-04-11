.. _serviceprovider :

Service Providers
-----------------

Web Processing Service (WPS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you provide directly a WPS via a standard interface, the platform will require the three operations that can be requested by a client and
performed by a WPS server, all mandatory implementation by all servers. Those operations are:

	- **GetCapabilities** – This operation allows the platform to request and receive back service metadata (or Capabilities) documents that describe the abilities of the specific server implementation. The GetCapabilities operation provides the names and general descriptions of each of the processes offered by a WPS instance. This operation also supports negotiation of the specification version being used for client-server interactions.

	- **DescribeProcess** – This operation allows the platform to request and receive back detailed information about the processes that can be run on the service instance, including the inputs required, their allowable formats, and the outputs that can be produced.

	- **Execute** – This operation allows the platform to run a specified process implemented by the WPS, using provided input parameter values and returning the outputs produced.


You will require only to provide the GetCapabilities endpoint url to the administrator of the platform to register it as a WPS provider.


Next sections describe the technical elements of the WPS operations that are important for the integration with the platform.



