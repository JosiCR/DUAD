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

Después de crear las tablas Cars, Owners y CarOwners, cada atributo depende únicamente
de la llave primaria de su tabla. No fue necesario realizar cambios adicionales, 
ya que no existen dependencias entre atributos que requieran separar una nueva entidad.



## Resultado Final

### Cars
VIN           Make        Model     Year    Color
------------  ----------  --------  ------  -------
1HGCM82633A   Honda       Accord    2003    Silver
5J6RM4H79EL   Honda       CR-V      2014    Blue
1G1RA6EH1FU   Chevrolet   Volt      2015    Red


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