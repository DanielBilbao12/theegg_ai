--Librerias a utilizar
with Ada.Text_IO;         use Ada.Text_IO;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Characters.Handling; use Ada.Characters.Handling;
with Ada.Strings.Maps; use Ada.Strings.Maps;

--PROBLEMAS POR CULPA DE EL RANGO DEL ARRAY, HAY QUE MIRAR COMO HACER QUE EL ARRAY SEA DINAMICO Y QUE NO HAGA FALTA DEFINIR SU RANGO. --> PATTERN ERROR--> Error debudo a que hay posiciones
--del array que al definir una longitud muy grande se quedan a "" y esto provoca el error de pattern, para arreglarlo, una vez definida la cadena, recortar los trozos en ""? (UNA OPCION)

procedure Main is

	package StringIlimitado renames Ada.Strings.Unbounded; use type StringIlimitado.Unbounded_String;

	--Variables y subprogramas
	type Subcadenas is array (Integer range<>) of Ada.Strings.Unbounded.Unbounded_String; --Tipo de Array de tamaño variable que almacena strings de tamaño no definido
	Subcadenas_Corta:Subcadenas(1..100);

	--Subprogramas
	procedure Identificar_Larga (Larga, Corta: in out StringIlimitado.Unbounded_String) is
		--Funcion para identificar que secuencia de ADN es mas larga
		aux : StringIlimitado.Unbounded_String;
	begin
		if Length(Larga) < Length(Corta) then
			aux:=Larga;
			Larga:=Corta;
			Corta:=aux;
		end if;
	end Identificar_Larga;

	function Comprobar_Secuencia (secuencia : StringIlimitado.Unbounded_String) return Boolean is
		--Funcion para comprobar que las secuencias de ADN introducidas estam unicamente compuestas de: 'A', 'C', 'G', 'T' y ' '
		correcto : Boolean:=False;
	begin
		for i in 1..Length(secuencia) loop
			if To_Upper(Element(secuencia,i))='A' or To_Upper(Element(secuencia,i))='C' or To_Upper(Element(secuencia,i))='G' or To_Upper(Element(secuencia,i))='T' or Element(secuencia,i)=' ' then
				correcto:=True;
			else
				Put_Line("ERROR, LA SECUENCIA DE ADN INTRODUCIA ES ERRONEA");
				return False;
			end if;
		end loop;
		return correcto;
	end Comprobar_Secuencia;

	procedure Encontrar_Subcadenas (secuencia : in StringIlimitado.Unbounded_String ; Subcadenas_Corta : in out Subcadenas)  is
	begin
		Subcadenas_Corta(1):= Ada.Strings.Unbounded.To_Unbounded_String("")&(Element(secuencia,1));
		for i in 2..Length(secuencia) loop
			Subcadenas_Corta(i):=Subcadenas_Corta(i-1)&Element(secuencia,i);
		end loop;
	end Encontrar_Subcadenas;

 procedure Encontrar_Mayor_Coincidencia (secuenciaLarga: in StringIlimitado.Unbounded_String ; Subcadenas_Corta : in Subcadenas ) is
		IndiceInicioCoincidencia: Integer:=0;
 begin
 	for i in reverse Subcadenas_Corta'Range loop --Evaluo desde la subcadena mas larga a la mas corta, si hay coincidencias, si no las hay el indice = 0
			IndiceInicioCoincidencia:= Index(secuenciaLarga, StringIlimitado.To_String(Subcadenas_Corta(i)));
			if IndiceInicioCoincidencia>0 then --Si indice>0, es que hay coincidencia entre la subcadena y la secuencia larga
				Put_Line("Coincidencia en la posicion:"&Integer'Image(IndiceInicioCoincidencia)&" de la secuencia larga con la subcadena: "&StringIlimitado.To_String(Subcadenas_Corta(i)));
				exit;
			end if;
		end loop;
		if IndiceInicioCoincidencia=0 then
			Put_Line("No hay coincidencias entre ambas secuencias de ADN");
		end if;
 end Encontrar_Mayor_Coincidencia;

	--Variables locales
	 secuenciaADN1 : StringIlimitado.Unbounded_String; --Secuencia larga
		secuenciaADN2 : StringIlimitado.Unbounded_String; --Secuencia corta
		MayorSecuenciaEnComun : StringIlimitado.Unbounded_String; --Resultado tras la comparación
begin
	--Codigo principal
	--Peticion de secuencias de ADN
	Put_Line("Introduzca la primera secuencia de ADN:");
	secuenciaADN1:= StringIlimitado.To_Unbounded_String(Get_Line);
	while Comprobar_Secuencia(secuenciaADN1)=False loop
			Put_Line("Introduzca la primera secuencia de ADN:");
	  secuenciaADN1:= StringIlimitado.To_Unbounded_String(Get_Line);
	end loop;
	Put_Line("Introduzca la segunda secuencia de ADN:");
	secuenciaADN2:= StringIlimitado.To_Unbounded_String(Get_Line);
	while Comprobar_Secuencia(secuenciaADN2)=False loop
			Put_Line("Introduzca la segunda secuencia de ADN:");
	  secuenciaADN2:= StringIlimitado.To_Unbounded_String(Get_Line);
	end loop;

	--Muestro las secuencias introducidas
	Identificar_Larga(secuenciaADN1, secuenciaADN2);
	Put_Line("La secuencia corta es:"&StringIlimitado.To_String(secuenciaADN2));
	Put_Line("LA secuencia larga es:"&StringIlimitado.To_String(secuenciaADN1));

	--Busco subcadenas en la secuencia mas corta
	Encontrar_Subcadenas(secuenciaADN2,Subcadenas_Corta);
	Put_Line("Las subcadenas encontradas en la secuencia de ADN mas corta son:");
	for i in 1..Length(secuenciaADN2) loop
		Put_Line("Cadena"&Integer'Image(i)&":"&StringIlimitado.To_String(Subcadenas_Corta(i)));
	end loop;

	--Busco y Muestro la mayor coincidencia entre ambas secuencias de ADN
  Encontrar_Mayor_Coincidencia(secuenciaADN1,Subcadenas_Corta);



end Main;
