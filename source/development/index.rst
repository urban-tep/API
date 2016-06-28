
Development
===========

.. toctree::
   :maxdepth: 2

The processor development environment of the Urban TEP is a virtual machine image that can be downloaded and run to develop, test and upload processors to Urban TEP processing centres. In the following subsections the processor interface is described. In addition, the interface used by the tools of the development environment to upload a processor package to a processing centre is defined. While the processor interface is generic, the internal upload interface is specific to the processing centre.

Processor descriptor structure
------------------------------

Each processor to be uploaded to a processing centre must be accompanied by a processor descriptor file. The processor descriptor is an XML file that declares name, parameters, calling convention, dependencies and other information of a processor. 

* An example of a descriptor XML can be found in :ref:`DescriptorXML`.
* The formal schema is available in :ref:`UrbantepXSD`. 

Important elements of the descriptor XML are:

  +-----------------------------+-----------------------------+-------------------------------------------------------------------+
  | Element name                |  Example                    | Description                                                       |
  +=============================+=============================+===================================================================+
  | /descriptor/processor       |                             |                                                                   |
  +-----------------------------+-----------------------------+-------------------------------------------------------------------+
  | ../processor/name           | Fmask8                      | name of the processor, for identification by user                 |
  +-----------------------------+-----------------------------+-------------------------------------------------------------------+
  | ../processor/executable     | fmask-and-merge.sh          | script or executable to be called                                 |
  +-----------------------------+-----------------------------+-------------------------------------------------------------------+
  | ../processor/parameters     |                             | structure for any number of parameter elements                    |
  +-----------------------------+-----------------------------+-------------------------------------------------------------------+
  | ..../parameter/name         | threshold                   | name of the parameter accepted by the processor                   |
  +-----------------------------+-----------------------------+-------------------------------------------------------------------+
  | ..../parameter/type         | string                      | one of boolean, string. Use string also for numbers.              |
  +-----------------------------+-----------------------------+-------------------------------------------------------------------+
  | ..../parameter/description  | cloud probability threshold | description of parameter for explanation                          |
  +-----------------------------+-----------------------------+-------------------------------------------------------------------+
  | ..../parameter/default      | 0.2                         | default value                                                     |
  +-----------------------------+-----------------------------+-------------------------------------------------------------------+
  | ../processor/packaging      |                             |                                                                   |
  +-----------------------------+-----------------------------+-------------------------------------------------------------------+
  | ..../packaging/name         | fmask                       | name of the processor package (for upload and deployment)         |
  +-----------------------------+-----------------------------+-------------------------------------------------------------------+
  | ..../packaging/version      | 3.2                         | version of the processor package (for deployment)                 |
  +-----------------------------+-----------------------------+-------------------------------------------------------------------+
  | ..../packaging/type         | Docker                      | currently, only Docker supported                                  |
  +-----------------------------+-----------------------------+-------------------------------------------------------------------+
  | ..../packaging/dependencies |                             | structure for any number of dependeny elements                    |
  +-----------------------------+-----------------------------+-------------------------------------------------------------------+
  | ....../dependency/name      | snap                        | name of required software, must be available in processing centre |
  +-----------------------------+-----------------------------+-------------------------------------------------------------------+
  | ....../dependency/version   | 4.0                         | version of required software, optional                            |
  +-----------------------------+-----------------------------+-------------------------------------------------------------------+
  | ..../packaging/resources    |                             | structure for any number of resource specifications               |
  +-----------------------------+-----------------------------+-------------------------------------------------------------------+
  | ....../resource/name        | memory                      | one of memory, timelimit                                          |
  +-----------------------------+-----------------------------+-------------------------------------------------------------------+
  | ....../resource/value       | 7000                        | value in MB, seconds respectively                                 |
  +-----------------------------+-----------------------------+-------------------------------------------------------------------+

Protocol information: Descriptor XML files are used as parameter to package and upload commands (see below).


Processor package structure
---------------------------

Upload command line interface
-----------------------------

Upload BC processing centre interface
-------------------------------------

Upload IT4I processing centre interface
---------------------------------------
