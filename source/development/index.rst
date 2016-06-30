
Development environment interfaces
==================================

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

A processor prepared for packaging is a directory that consists of

 * the runtime software of the processor in a subdirectory tree <package-name>-<package-version>, with shared libraries, scripts, auxiliary data, etc.
 * as part of this a script to be called with the input product as first command line argument (the one listed as processor/executable in the descriptor XML), and a parameters file as optional second argument (with key=value lines in it)
 * a Dockerfile (outside of the subdirectory) that sets up a basic operating system (e.g. centos:7) and installs additional libraries necessary for the processor
 * a descriptor.xml file (outside of the subdirectory)

Example::

    myprocessor/fmask-3.2/fmask-and-merge.sh
                         /Fmask
                         /run_Fmask.sh
                         /merge-graph.xml
               /Dockerfile
               /descriptor.xml

This is the processing centre-independent structure of an Urban TEP processor.

The packaging (see command line interface below) creates from this a processing centre-specific package zip file. This is the interface item to be uploaded from the development environment to the processing centre for deployment. For the BC processing centre it consists of

 * a .tar.gz file with the content of the runtime processor directory tree
 * a .tar.gz file that contains the Dockerfile
 * a bundle-descriptor.xml file generated from the descriptor.xml, but specific to the BC processing centre
 * a wrapper script generated from the descriptor.xml, adapter between Calvalus and the processor

Example urbantep-fmask-3.2.zip::

    Archive:  urbantep-fmask-3.2.zip
      Length      Date    Time    Name
    ---------  ---------- -----   ----
      7793939  05-03-2016 15:38   urbantep-fmask-3.2.tar.gz
          185  05-03-2016 15:38   urbantep-fmask-package-info.tar.gz
         1401  05-03-2016 15:38   bundle-descriptor.xml
          914  05-03-2016 15:38   Fmask8-process.vm
    ---------                     -------
      7796439                     4 files

Processor calling convention
----------------------------

At runtime the executable of the processor will be called in a working directory that contains the input file and where any intermediate files and the output can be placed. The calling signature is

  <executable> <input-product> <parameters-file>

Example::

  fmask-3.2/fmask-and-merge.sh LC81840512016168LGN00.tgz parameters

parameters is a file that contains one parameter per line as key=value

Example::

  threshold=0.2
  buffer=5

In order to identify the result file(s) of processing the executable shall use the tag OUTPUT_PRODUCT at the beginning of a line, followed by the filename of the result. Several OUTPUT_PRODUCT lines can be used to identify several files as result. If the executable is a Bash script it may use::

  . $2

to convert all parameters to environment variables available in the script, and::

  echo "OUTPUT_PRODUCT <result-file>"

to identify the result.

Processors must not modify their runtime software directory tree in any way. They must only write to the working directory or may create subdirectories of the working directory. They do not need to clean up afterwards.

Upload command line interface
-----------------------------

The command line interface to package a processor prepared for packaging and to upload a processor package consists of two tools specific to the target processing centre. For the BC processing centre these are package-bc.sh and upload-bc.sh.

  package-bc.sh <descriptor file>

Example::

  cd myprocessor
  package-bc.sh descriptor.xml

The upload command has the signature

  upload-bc.sh <descriptor file>

Example::

  cd myprocessor
  upload-bc.sh descriptor.xml

The upload-bc.sh tool will ask for user name and password. The user must be registered with the respective processing centre.

Note that these two tools use the structure of processors prepared for packaging defined above as interface item on the user side, and the processor package as interface item towards the processing centre. Behind the scenes the upload tool uses the upload BC processing centre interface defined next.

Upload BC processing centre interface
-------------------------------------

The upload interface is a HTTP POST interface with authentication to upload processor package zip files to the BC procesing centre for automated deployment. Endpoint of the interface is

  http://www.brockmann-consult.de:80/calvalus/calvalus/upload?dir0software&bundle=true

The processor package zip file is to be provided as multipart/form-data .

The challenge for user name and password shall use the cookie returned by the first request and authenticate at 

  http://www.brockmann-consult.de:80/calvalus/j_security_check

with POST message formatted as

  j_username=<user-name>&j_password=<password>&submitBtn=Log+In



Upload IT4I processing centre interface
---------------------------------------

This interface is planned for a later version of the Urban TEP.
