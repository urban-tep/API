
Interface Overview
==================

.. toctree::
   :maxdepth: 2

Urban Thematic Exploitation Platform concept
--------------------------------------------
 
The Urban TEP is a platform for the “urban analysis” user community. It provides various urban products, but also Earth Observation data from various sensors and missions and reference data useful to generate higher level urban products.

The Urban TEP comprises a portal and information system, and it provides (three) processing centres. With their functions they allow to test new ideas, process EO data with thematic proces-sors without the need to download the data beforehand, and visualize, analyse and combine the results in a Web GIS. In addition it supports the integration of user algorithms, the publication of data products generated, up to the provision of new processing services.

The TEP Urban concept is based on a generic, modular, multi-purpose design facilitating flexibility with respect to the adaptation to and integration of user requirements, application scenarios, processing and analysis technologies, and IT infrastructures. Considering the thematic and technical objectives of TEP Urban the essential elements of the Urban TEP are:

 - Web-based platform to access, explore, generate, analyse, validate and visualize geospatial data (in particular EO imagery) and derived products.
 - Processing infrastructure for very fast, cost effective and operational i) access to multiple satellite mission archives (in particular ESA and Sentinel archives), and ii) implementation and operation of VA processors.
 - Thematic value-adding processors providing geo-information products on the urban environment and its development.
 - Expert knowledge and user community integration by means of active target community participation.

Urban TEP Use cases  
-------------------

Based on the dialogue with user communities the main user stories and use cases of the platform have been defined and consolidated in the Systems and Services TN [TSS 2015]. The use cases identified are

 - UC-01: Query and access existing thematic content, with two applications: 
   - KPA1: Access an accurate settlements map, and 
   - KPA2: Get information on settlements properties and patterns

 - UC-02: Conduct on-demand processing, with three applications:
   - KPA1: Generate temporal statistics baseline product
   - KPA2: Generate settlements mask
   - KPA3: Quantify imperviousness/urban greenness

 - UC-03: Develop and deploy a new service and/or new product with the application:
   - KPA1: Generate functional urban areas service and related baseline product

 - UC-04: Combine, analyse and visualise data, products and results, with the application:
   - KPA7: Visualization and WebGIS functionalities
   - KPA8: Communication and/or connection of WBG’s Platform for Urban Mapping and Analysis (PUMA) with TEP Urban platform/products/services.

These use cases are an important source for the thematic Urban TEP requirements and thus of the verification plan.

System decomposition
--------------------

The Urban TEP system is decomposed into subsystems and functional components. The interfaces between these subsystems are subject of this ICD. The top level subsystems of the Urban TEP are:

 - Urban TEP Portal 
 - Urban TEP Data Gateway
 - Urban TEP Reporting
 - PUMA
 - Urban TEP DLR Processing Centre
 - Urban TEP BC Processing Centre
 - Urban TEP IT4I Processing Centre

The Urban TEP Portal subsystem is the top-level component of the system.
The portal is the frontend for the users where they will find the information pages, discover the thematic applications, participate in the thematic groups and interact with other users. The portal provides a work environment for users, enabling them to perform data-intensive research by running dedicated processing software on ready to be used Earth Observation data resources.
 
The Urban TEP Processing Centres are based on slightly different architectures and with different Earth observation datasets and processing workflows available. The DLR processing centre is based on GeoFarm and a Calvalus processing system. The BC processing centre is based on Calvalus. And the IT4I processing centre is based on an HPC cluster. Nevertheless, the Urban TEP processing centres provide a uniform interface, concurrent processing on computer clusters, a common set of functions, and a uniform way to develop processors.

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
