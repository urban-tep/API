
Overview
=========

.. toctree::
   :maxdepth: 2

This Urban TEP ICD describes the interfaces of the different Urban TEP subsystems. Each interface is described by its purpose, the interface items exchanged, and the protocol used. Description is done by example and explanation specific to Urban TEP. For formal definitions the used standard provides the complementary formal definitions.

This ICD assumes that readers are familiary with the Urban TEP SDD. Please refer to the SDD for the context of the interface information.

Interface overview
------------------

The following diagram shows a logical view of the main external and internal interfaces of the Urban TEP.

.. include:: interface_diagram.rst

The main paths through the Urban TEP are:

 - User information using the Web GUI from user to portal and the OpenSearch interface of the catalogue
 - Processing using the Web GUI from user to portal and and further to the processing centres via the WPS interface
 - Analysis and visualisation using the Web GUI from the user to the portal and further to PUMA where users have direct access to the analysis results
 - Data interfaces between processing centres and data providers, and further via data gateway and portal to PUMA or the user
 - Processor upload from the processor development environment to processing centres.

There are additional interfaces for reporting and user relationship management and issue tracking. These interfaces are described in the following chapters.
