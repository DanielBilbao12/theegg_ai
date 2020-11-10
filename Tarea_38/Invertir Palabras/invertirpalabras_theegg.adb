--Declaracion de librerias
with Ada.Text_IO;         use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;
with Ada.Strings.Unbounded;
with GNAT.String_Split;   use GNAT;

procedure InvertirPalabras_theegg is
   --Declaracion de variables globales
   package StringIlimitado renames Ada.Strings.Unbounded;
   use type StringIlimitado.Unbounded_String;
   FraseUsuario   : StringIlimitado.Unbounded_String;
   NumeroDeFrases : Natural;
   palabras       : String_Split.Slice_Set;
   cEspera        : Character;

   --Declaracion de subprogramas
   procedure SepararString (frase : String; separador : String) is
   begin
      String_Split.Create
        (S    => palabras, From => frase, Separators => separador,
         Mode => String_Split.Multiple);
      --Put_Line("De la frase se obtienen"&String_Split.Slice_Number'Image(String_Split.Slice_Count(palabras))&" palabras");
      for i in reverse 1 .. String_Split.Slice_Count (palabras) loop
         declare
            palabra : constant String := String_Split.Slice (palabras, i);
         begin
            Put (palabra);
            Put (" ");
         end;
      end loop;
   end SepararString;

begin
   --Codigo a ejecutar
   Put ("Introduzca el numero de frases a invertir:");
   Get (NumeroDeFrases);
   Skip_Line;
   for i in 1 .. NumeroDeFrases loop
      Put ("Introduzca la" & Integer'Image (i) & " frase:");
      FraseUsuario := StringIlimitado.To_Unbounded_String (Get_Line);
      Put ("Case #" & Integer'Image (i) & ": ");
      SepararString (StringIlimitado.To_String (FraseUsuario), " ");
      New_Line;
   end loop;
   Put ("Pulse cualquier tecla para salir del programa..");
   Get_Immediate (cEspera); -- Pulsar una tecla para finalizar
end InvertirPalabras_theegg;
