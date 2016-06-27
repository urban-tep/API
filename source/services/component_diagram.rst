.. uml::

    @startuml

        !include ../../includes/skins.iuml

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

            USER .down.> PUMA
            USER .down.> PORTAL
            USER .down.> ISSTRACK
            PUMA .down.> DATGAT

            PORTAL .left.> PUMA
            PORTAL .down.> ISSTRACK
            PORTAL .down.> CAT
            PORTAL .down.> APEL
            PORTAL .down.> PC
            PORTAL .down.> DATGAT

            DATGAT .down.> PC
            DATGAT .down.> DATPROV

            CAT .right.> DATGAT
            CAT .down.> PC

            PC .up.> APEL
            PC .up.> ISSTRACK

            PC .down.> DATPROV
        }
    @enduml