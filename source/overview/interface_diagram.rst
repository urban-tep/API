.. uml::

    :caption: Urban TEP Interface Diagram
    :width: 16cm
    :align: center

    !include includes/skins.iuml

    skinparam backgroundColor #FFFFFF
    skinparam componentStyle uml2

    skinparam interface {
      backgroundColor<<USER>> Green
      borderColor<<USER>> DarkGreen
    }

    interface "User" as USER <<USER>>
    [Data Provider] as DATPROV

    package "Urban TEP" {
        [Portal] as PORTAL
        [PUMA] as PUMA
        [Catalogue] as CAT
        [Reporting] as APEL
        [Processing Center] as PC
        [Data Gateway] as DATGAT
        [Issue Tracker] as ISSTRACK
        [Devel Env] as DEVENV

        USER .down.> PUMA : Web GUI
        USER .down.> PORTAL : Web GUI
        USER .down.> ISSTRACK

        PUMA .down.> DATGAT : result retrieval
        PUMA .down.> CAT
        PUMA .down.> APEL

        PORTAL .right.> PUMA : analysis and visualisation request
        PORTAL .down.> ISSTRACK
        PORTAL .down.> CAT : search
        PORTAL .down.> APEL : report access
        PORTAL .down.> PC : production request, result metadata
        PORTAL .down.> DATGAT : result retrieval

        DATGAT .down.> PC

        PC .up.> APEL
        PC .up.> ISSTRACK
        PC .up.> CAT
        PC .down.> DATPROV : EO data product harvesting

        DEVENV .left.> PC : processor upload
    }

