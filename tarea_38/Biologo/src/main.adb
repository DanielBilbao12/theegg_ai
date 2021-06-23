--Librerias a utilizar
with Ada.Text_IO;         use Ada.Text_IO;
with Ada.Strings.Unbounded;

procedure Main is

	package StringIlimitado renames Ada.Strings.Unbounded; use type StringIlimitado.Unbounded_String;

	--Variables y subprogramas

	--Subprogramas
	procedure Identificar_Larga (Larga, Corta: in out String) is
		aux : String:="";
	begin
		if Larga'Last < Corta'Last then
			aux:=Larga;
			Larga:=Corta;
			Corta:=aux;
		end if;
	end Identificar_Larga;

	--Variables locales
	secuenciaADN1 : StringIlimitado.Unbounded_String; --Secuencia larga
	secuenciaADN2 : StringIlimitado.Unbounded_String; --Secuencia corta
begin
	--Codigo principal
	--Peticion de secuencias de ADN
	Put_Line("Introduzca la primera secuencia de ADN:");
	secuenciaADN1:= StringIlimitado.To_Unbounded_String(Get_Line);
	Put_Line("Introduzca la segunda secuencia de ADN:");
	secuenciaADN2:= StringIlimitado.To_Unbounded_String(Get_Line);
	--Muestro las secuencias introducidas
	Put_Line("La secuencia corta es :"&StringIlimitado.To_String(secuenciaADN2));
	Put_Line("LA secuencia larga es:"&StringIlimitado.To_String(secuenciaADN1));

end Main;
