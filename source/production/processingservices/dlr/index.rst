
DLR Provider
============

.. toctree::
   :maxdepth: 2

General Remarks
^^^^^^^^^^^^^^^

DLR uses the same software and hardware cluster as Brockmann Consult. The configuration and usage of the Calvalus Processing System at DLR follows the same conventions and standards as the Brockmann Consult System. 

Services Discovery
^^^^^^^^^^^^^^^^^^

- WPS getCapabilities

See http://docs.terradue.com/esa-tep-urban-api/production/processingservices/bc/index.html#services-discovery

Service Description
^^^^^^^^^^^^^^^^^^^

- WPS describeProcess

See http://docs.terradue.com/esa-tep-urban-api/production/processingservices/bc/index.html#service-description

Processing Execution
^^^^^^^^^^^^^^^^^^^^

- WPS execute

See http://docs.terradue.com/esa-tep-urban-api/production/processingservices/bc/index.html#processing-execution

Result Retrieval
^^^^^^^^^^^^^^^^

- WPS retrieveResult and Download

See http://docs.terradue.com/esa-tep-urban-api/production/processingservices/bc/index.html#result-status-retrieval

Managing Cache
^^^^^^^^^^^^^^

Processes whose products need to be cached can be monitored by a cronjob that deletes all remnants older than a given time

Call::
  
  crontab -e

Entry for a cache to be monitored every 5 minutes. Deletes all tifs older than an hour in specific directory::

   */5 * * * * find /foo/bar/ -mmin +60 -name "*.tif" | xargs -I% rm %

FTP based Push Service
^^^^^^^^^^^^^^^^^^^^^^

Push Services (e.g. ESA GPOD) publishing to a FTP Server can be managed via crontab and a simple sript

:ref:`ftp`
