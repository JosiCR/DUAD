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


### CarOwners (Actualizada)
VIN           OwnerID
------------  ---------
1HGCM82633A   101
1HGCM82633A   102
5J6RM4H79EL   103
1G1RA6EH1FU   104


## Tercera Forma Normal (3FN)
Justificación

Se identificó que los atributos Make, Model y Year describen el modelo del vehículo y no al vehículo identificado por el VIN.
Por eso, se creó la tabla CarModels y la tabla Cars pasó a almacenar únicamente una referencia al modelo mediante ModelID.

Además, se identificó que la información de la póliza de seguro puede ser compartida por varios propietarios. Para evitar repetir 
la compañía de seguros y la póliza en cada propietario, se creó la tabla InsurancePolicies y la tabla Owners pasó a almacenar 
únicamente PolicyID como referencia.


### Cars Models
ModelID     Make         Model      Year
----------  -----------  ---------  ------
1           Honda        Accord     2003
2           Honda        CR-V       2014
3           Chevrolet    Volt       2015


### Cars
VIN           ModelID    Color
------------  ---------  -------
1HGCM82633A   1          Silver
5J6RM4H79EL   2          Blue
1G1RA6EH1FU   3          Red


### InsurancePolicies
PolicyID    InsuranceCompany    InsurancePolicy
----------  ------------------  ----------------
1           ABC Insurance       Fire & Theft
2           XYZ Insurance       Full Cover
3           DEF Insurance       Collision
4           GHI Insurance       Basic Legal


### Owners
OwnerID      OwnerName    OwnerPhone     PolicyID
-----------  -----------  -------------  --------
101          Alice        123-456-7890   1
102          Bob          987-654-3210   2
103          Claire       555-123-4567   3
104          Dave         111-222-3333   4


## Resultado Final

### Cars Models
ModelID     Make         Model      Year
----------  -----------  ---------  ------
1           Honda        Accord     2003
2           Honda        CR-V       2014
3           Chevrolet    Volt       2015


### Cars
VIN           ModelID    Color
------------  ---------  -------
1HGCM82633A   1          Silver
5J6RM4H79EL   2          Blue
1G1RA6EH1FU   3          Red


### InsurancePolicies
PolicyID    InsuranceCompany    InsurancePolicy
----------  ------------------  ----------------
1           ABC Insurance       Fire & Theft
2           XYZ Insurance       Full Cover
3           DEF Insurance       Collision
4           GHI Insurance       Basic Legal


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