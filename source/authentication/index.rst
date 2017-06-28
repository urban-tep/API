
Plan to reduce number of accounts for a User
============================================

.. toctree::
   :maxdepth: 2

Users authenticate against the Urban TEP web portal using ESA EO SSO. This way users have to authenticate only once when using services like the portal or the visualisation and analysis tools. But there are some other elements in the Urban TEP that do not depend on EO SSO that certain users interact with in certain situations. These are:

* The processing centres to upload a processor
* The data agent to proxy processing result access
* The ticket system to search for support

The elimination of these accounts has administrative implications and technical implications. Administratively, the corresponding subsystems either have to trust any self-registered ESA user, or they have to trust the portal where it serves as a gateway that it properly checks authorisation, or they build their own way to check whether a user is authorised for an action other than the capability to "log in" and use an interface. Technically, this either involves the integration of the ESA EO-SSO as identity provider into the web interface of the service, or the use of the portal as a proxy for all protected requests.

The following subsections explain the technical aspects.

Avoiding additional processing centre accounts
----------------------------------------------

The processing centres can either use the portal as a proxy for processor package upload, or they implement ESA EO-SSO in their web interface for processor upload and WPS access. 

* The former requires updates to the portal that has to forward HTTP POST requests with larger payload to the respective processing centre (for processor upload). Internally, the proxying portal uses the system account of the processing centre with the remote_user attribute. 
* The latter involves adding the layer and configuration to the web servers of the processing centre to redirect unauthenticated calls and accept ESA EO SSO identities directly. 

In both cases an authorisation check for each function has to be introduced as any EO SSO self-registered user now may try to use this interface. The authorisation check can be accomplished by the introduction of additonal groups in LDAP (tep_processor_developers, ...) and by checking for group membership in the different functions available in the WEB interface.

The tools that automate the use of the interface have to be modified to simulate the browser single-sign-on procedure. Since EO SSO is not one of the standard protocols supported by tools like wget or curl, the sequence of interactions usually done by a browser has to be implemented by repeated HTTP(S) calls and response analyses.

Avoiding the Terradue Cloud Platform accounts
---------------------------------------------

The portal and data agent can exchange API keys in order to avoid a second login when using the Terradue cloud platform for data access. When a user links his Terradue account in the platform then TEP will import the API key and use it for the calls to Terradue Cloud platform.

Avoiding the ticket system accounts
-----------------------------------

The ticket system is based on Redmine. Redmine supports several types of authentication methods (LDAP, AD, SSO, ...). Some are built-in and some are available via plugins. So it should be possible to connect Redmine to a central authentication system such as ESA SSO.

Implementation schedule
-----------------------

Some of these means may already be implemented during pre-operations. Else, they are an option.
