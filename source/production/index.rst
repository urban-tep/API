.. _productionapi :


Production API
==============


The Production API covers many use cases for the usage of the processing service of the platform. They are described in the following diagram.

.. uml::
  :caption: Production API use cases

   !include includes/skins.iuml

   skinparam backgroundColor #FFFFFF
   skinparam componentStyle uml2

   actor User

   rectangle user {
     (Discover Providers) as UCDP
     User -> UCDP
     (Describe Processing Services) as UCDS
     User -> UCDS
     (Execute Process) as UCEP
     User -> UCEP
   }

   actor Provider

   rectangle provider {
     (Register as a Provider) as UCRP
     UCRP <- Provider
     (Expose Processing Services) as UCES
     UCES <- Provider
     (Deliver Results) as UCDR
     UCDR <- Provider
   }

   UCDP .. UCRP
   UCDS .. UCES
   UCEP .. UCDR


As shown in previous diagram there are mainly 2 actors:

- **Service User** that discovers the service Available via the portal API,
- **Service Provider** that promote services and deliver processing results via the portal API.


So far, the interface to provide a processing service is via Web Processing Service (WPS) [#OGCWPS]_



.. toctree::
   :maxdepth: 2

   ../external/t2api/source/production/concepts/index
   serviceprovider
   ../external/t2api/source/production/providingwps
   ../external/t2api/source/production/processexecution
   ../external/t2api/source/production/resultdelivery
   ../external/t2api/source/production/usingwps
   processingservices/index
   
   
   
   

.. rubric:: Footnotes

.. [#OGCWPS] http://www.opengeospatial.org/standards/wps

