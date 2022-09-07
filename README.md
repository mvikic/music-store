Python console application for a musical instruments store 
=======

Getting started
------

Open a command prompt window with the cwd set to the path of the project files.

Creat an user account with option (1). Then log on to that user account using the before created credentials.
Three account roles are available: buyer (kupac), seller (prodavac) and manager (menadžer). 
A buyer account can be created directly using the console. The manager creates an account for the seller, and the manager role is set up in the korisnici.txt file.

Functionalities:
- Registration of a new buyer (username, pass, name, surname)
- Storing and retrieving user data from a simple text file
- Login for buyers, managers and clerks
- All roles: - show all instruments in stock
             - search for instruments by code, name, manufacturer and type
    - Buyer only: - buy instrument(s)
                  - see previous purchases
    - Manager only: - show all instruments in stock and out of stock
                    - add new account for clerk
                    - print a report for all purchases
    - Clerk only: - show all instruments in stock and out of stock
                  - add new, edit existing and logically delete an instrument
