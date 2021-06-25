--Librerias a utilizar
with Ada.Text_IO;         use Ada.Text_IO;
with Ada.Strings.Unbounded; use Ada.Strings.Unbounded;
with Ada.Characters.Handling; use Ada.Characters.Handling;
with Ada.Strings.Maps; use Ada.Strings.Maps;
with Ada.Strings.Fixed; use Ada.Strings.Fixed;

--ERROR YA QUE NO CONSIGO TODAS LAS SUBCADENAS DENTRO DE LA SECUENCIA DE ADN.--> AL CAMBIAR ESTO, TENDRE QUE MODIFICAR LA ULTIMA FUNCION QUE IDENTIFICA SI HAY COINCIDENCIAS

procedure Main is

	package StringIlimitado renames Ada.Strings.Unbounded; use type StringIlimitado.Unbounded_String;

	--Variables y subprogramas
	TamañoArray: Integer:=0; --Ponemos array de 1 a 10 por defecto
	type Subcadenas is array (Integer range<>) of Ada.Strings.Unbounded.Unbounded_String; --Tipo de Array de tamaño variable que almacena strings de tamaño no definido

	--Subprogramas
	procedure Identificar_Larga (Larga, Corta: in out StringIlimitado.Unbounded_String ; LongitudArray : in out Integer) is
		--Funcion para identificar que secuencia de ADN es mas larga
		aux : StringIlimitado.Unbounded_String;
	begin
		if Length(Larga) < Length(Corta) then
			aux:=Larga;
			Larga:=Corta;
			Corta:=aux;
		end if;
		--Defino la longitud del array que almacena todas las subcadenas de la secuencia mas corta
		for i in 1..Length(Corta) loop
			LongitudArray:=LongitudArray+i;
		end loop;
		LongitudArray:= LongitudArray-1;
		--Put_Line("El rango del array que almacena las subcadenas es de:"&Integer'Image(LongitudArray));
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

	procedure Encontrar_Subcadenas (secuencia : in StringIlimitado.Unbounded_String ; Subcadenas_Corta : in out Subcadenas; RangoArray : Integer)  is
		cont : Integer:=2;
	begin
		for i in 1..Length(secuencia) loop
			for k in i..RangoArray loop
				Subcadenas_Corta(k):=Ada.Strings.Unbounded.To_Unbounded_String(Slice(secuencia,1,i));
			end loop;
			for k in Length(secuencia)+1..RangoArray loop
				Subcadenas_Corta(k):=Ada.Strings.Unbounded.To_Unbounded_String(Slice(secuencia,2,i));
			end loop;
			for k in Length(secuencia)+2..RangoArray loop
				Subcadenas_Corta(k):=Ada.Strings.Unbounded.To_Unbounded_String(Slice(secuencia,3,i));
			end loop;
			for k in Length(secuencia)+3..RangoArray loop
				Subcadenas_Corta(k):=Ada.Strings.Unbounded.To_Unbounded_String(Slice(secuencia,4,i));
			end loop;
--FALTAN COMBINACIONES, DE AQUI HAY QUE COGER LA IDEA DE LOS SLICE, QUE PERMITE PARTIR EL STRING DE MANERA SENCILLA
		end loop;







	end Encontrar_Subcadenas;


 procedure Encontrar_Mayor_Coincidencia (secuenciaLarga: in StringIlimitado.Unbounded_String ; Subcadenas_Corta : in Subcadenas ) is --Tendre que modificarla porque el array de subcadenas ya o esta ordenado de mas largo a mas corto...
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
	Identificar_Larga(secuenciaADN1, secuenciaADN2, TamañoArray);
	Put_Line("La secuencia corta es:"&StringIlimitado.To_String(secuenciaADN2));
	Put_Line("LA secuencia larga es:"&StringIlimitado.To_String(secuenciaADN1));
	declare
		Subcadenas_Corta:Subcadenas(1..TamañoArray);
	begin
	Encontrar_Subcadenas(secuenciaADN2, Subcadenas_Corta, TamañoArray);
	Put_Line("Las subcadenas encontradas en la secuencia de ADN mas corta son:");
	for i in Subcadenas_Corta'Range loop
		Put_Line("Cadena"&Integer'Image(i)&":"&StringIlimitado.To_String(Subcadenas_Corta(i)));
	end loop;
	--Busco y Muestro la mayor coincidencia entre ambas secuencias de ADN
		Encontrar_Mayor_Coincidencia(secuenciaADN1,Subcadenas_Corta);
	end;
end Main;
