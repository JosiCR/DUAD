### Ejercicio Cars

## Tabla original
VIN           Make        Model     Year    Color    Owner ID    Owner Name    Owner Phone     Insurance Company    Insurance Policy
------------  ----------  --------  ------  -------  ----------  ------------  --------------  -------------------  ----------------
1HGCM82633A   Honda       Accord    2003    Silver   101         Alice         123-456-7890    ABC Insurance        Fire & Theft
1HGCM82633A   Honda       Accord    2003    Silver   102         Bob           987-654-3210    XYZ Insurance        Full Cover
5J6RM4H79EL   Honda       CR-V      2014    Blue     103         Claire        555-123-4567    DEF Insurance        Collision
1G1RA6EH1FU   Chevrolet   Volt      2015    Red      104         Dave          111-222-3333    GHI Insurance        Basic Legal



## Primera Forma Normal (1FN)
Justificación

separe la información del vehículo de la información de los propietarios 
porque un mismo vehículo puede estar asociado a diferentes propietarios. 
De esta forma, los datos del vehículo se almacenan una sola vez y la relación 
con los propietarios se maneja en una tabla independiente.


### cars
VIN           Make        Model     Year    Color
------------  ----------  --------  ------  -------
1HGCM82633A   Honda       Accord    2003    Silver
5J6RM4H79EL   Honda       CR-V      2014    Blue
1G1RA6EH1FU   Chevrolet   Volt      2015    Red


### CarOwners
VIN           OwnerID    OwnerName    OwnerPhone     InsuranceCompany    InsurancePolicy
------------  ---------  -----------  -------------  ------------------  ----------------
1HGCM82633A   101        Alice        123-456-7890   ABC Insurance       Fire & Theft
1HGCM82633A   102        Bob          987-654-3210   XYZ Insurance       Full Cover
5J6RM4H79EL   103        Claire       555-123-4567   DEF Insurance       Collision
1G1RA6EH1FU   104        Dave         111-222-3333   GHI Insurance       Basic Legal


## Segunda Forma Normal (2FN)
Justificación

hice la tabla Owners porque el nombre del propietario, su teléfono, la compañía de seguros
y la póliza dependen únicamente del OwnerID. Si estos datos permanecieran en CarOwners, 
se repetirían cada vez que un propietario estuviera asociado a un vehículo por eso, 
CarOwners conserva únicamente la relación entre el vehículo y el propietario.


### Owners
OwnerID      OwnerName    OwnerPhone     InsuranceCompany    InsurancePolicy
-----------  -----------  -------------  ------------------  ----------------
101          Alice        123-456-7890   ABC Insurance       Fire & Theft
102          Bob          987-654-3210   XYZ Insurance       Full Cover
103          Claire       555-123-4567   DEF Insurance       Collision
104          Dave         111-222-3333   GHI Insurance       Basic Legal


### CarOwners 
VIN           OwnerID
------------  ---------
1HGCM82633A   101
1HGCM82633A   102
5J6RM4H79EL   103
1G1RA6EH1FU   104


## Tercera Forma Normal (3FN)
Justificación

Se separaron las marcas y las compañías de seguros en tablas independientes para evitar 
la repetición de información. Cars Models utiliza MakeID para relacionarse con Makes, 
mientras que InsurancePolicies utiliza CompanyID para relacionarse con InsuranceCompanies. 
De esta forma, una misma marca puede tener varios modelos y una misma compañía puede tener 
varias pólizas sin duplicar sus datos.

### Makes
MakeID      Make
------      ---------
1           Honda
2           Chevrolet


### Cars Models
ModelID     MakeID      Model       Year
--------    --------    ---------   ------
1           1           Accord      2003
2           1           CR-V        2014
3           2           Volt        2015


### Cars
VIN           ModelID    Color
------------  ---------  -------
1HGCM82633A   1          Silver
5J6RM4H79EL   2          Blue
1G1RA6EH1FU   3          Red


### InsuranceCompanies
CompanyID    CompanyName
---------    --------------
1            ABC Insurance
2            XYZ Insurance
3            DEF Insurance
4            GHI Insurance


### InsurancePolicies
PolicyID    CompanyID    InsurancePolicy
--------    ---------    ----------------
1           1            Fire & Theft
2           2            Full Cover
3           3            Collision
4           4            Basic Legal


### Owners
OwnerID      OwnerName    OwnerPhone     PolicyID
-----------  -----------  -------------  --------
101          Alice        123-456-7890   1
102          Bob          987-654-3210   2
103          Claire       555-123-4567   3
104          Dave         111-222-3333   4


## Resultado Final


### Makes
MakeID      Make
------      ---------
1           Honda
2           Chevrolet


### Cars Models
ModelID     MakeID      Model       Year
--------    --------    ---------   ------
1           1           Accord      2003
2           1           CR-V        2014
3           2           Volt        2015


### Cars
VIN           ModelID     Color
------------  ---------   -------
1HGCM82633A   1           Silver
5J6RM4H79EL   2           Blue
1G1RA6EH1FU   3           Red


### InsuranceCompanies
CompanyID    CompanyName
---------    --------------
1            ABC Insurance
2            XYZ Insurance
3            DEF Insurance
4            GHI Insurance


### InsurancePolicies
PolicyID    CompanyID    InsurancePolicy
--------    ---------    ----------------
1           1            Fire & Theft
2           2            Full Cover
3           3            Collision
4           4            Basic Legal


### Owners
OwnerID      OwnerName    OwnerPhone     PolicyID
-----------  -----------  -------------  --------
101          Alice        123-456-7890   1
102          Bob          987-654-3210   2
103          Claire       555-123-4567   3
104          Dave         111-222-3333   4


### CarOwners
VIN           OwnerID
------------  ---------
1HGCM82633A   101
1HGCM82633A   102
5J6RM4H79EL   103
1G1RA6EH1FU   104