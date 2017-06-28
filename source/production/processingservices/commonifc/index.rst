
Common Processing centre interfaces
==============================================

.. toctree::
   :maxdepth: 2

User identification and authentication for OGC WPS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The portal is the gateway for users to the processing centre. A user fills a form in the portal that in turn submits a request to the WPS of a processing centre. 

The OGC WPS interface does not define how to transfer user information and how to do authentication. For the Urban TEP the following interface is defined for this:

- The processing centre uses HTTP basic authentication for all WPS requests (GetCapabilities, DescribeProcess, Execute), status requests (HTTP GET), and result retrieval requests (HTTP GET).
- The user name and password provided for basic authentication is a "system user" with a password only used by the portal system. This is transferred in the standard header *Authorization*. The system user shall be "utepportal".
- The name of the external user that is registered with EO-SSO and that is logged in in the portal is transferred in the additional HTTP header field *Remote_user*.
- The processing centre can access additional information about this user in the user profile retrieval interface provided by the portal. This information may be relevant to grant access rights to data and processors.

  +---------------------------+--------------------------------------------------------------------------------+
  | Element name              |  Description                                                                   |
  +===========================+================================================================================+
  | Authorization             | HTTP basic authentication header field containing the string 'Basic' and an    |
  |                           | encoded string username:password . The username is the "system user"           |
  |                           | "utepportal" for all requests arriving from the portal.                        |
  +---------------------------+--------------------------------------------------------------------------------+
  | Remote_user               | Header field with the external user name as registered in EO-SSO and logged in |
  |                           | in the portal.                                                                 |
  +---------------------------+--------------------------------------------------------------------------------+


Processing result metadata records
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The result metadata record is an XML document following the Atom feed structure with an OGC Observations and Measurements content. An example is provided in :ref:`appendix-b`.



