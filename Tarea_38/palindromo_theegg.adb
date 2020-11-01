--Librerias a usar
with Ada.Text_IO;         use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;
procedure Palindromo_TheEgg is
   --Variables globales
   nUsuario : Integer;
   kont     : Integer;
   --Subprogramas
   function InvertirNumero (x : Integer) return Integer is
      alreves, num : Integer;
   begin
      num     := x;
      alreves := 0;
      while num /= 0 loop
         alreves :=
           (alreves * 10) +
           num mod
             10; --El operando mod consigue el resto, en este caso el resto de dividir num entre 10
         num := num / 10;
      end loop;
      return alreves;
   end InvertirNumero;

   function EsPalindromo (x : Positive) return Boolean is
   begin
      --Un numero es palindromo si es igual que su reverso
      if x = InvertirNumero (x) then
         return True;
      else
         return False;
      end if;
   end EsPalindromo;

   function EsPrimo (numero : Positive) return Boolean is
   begin
      kont := 0;
      for i in 1 .. numero loop
         if numero rem i = 0 then
            kont := kont + 1;
         end if;
      end loop;
      if kont = 2 then
         return True;
      else
         return False;
      end if;
   end EsPrimo;

begin
   --Codigo a ejecutar
   Put ("Introduzca un numero entero positivo: ");
   Get (nUsuario);
   --Ejecucion del algoritmo que devuelve el resultado el palindromo primo mas pequeño (mayor o igual que N)
   for i in nUsuario .. 5_000_000
   loop --Ejecuto el bucle for hasta un numero muy alto para poder evaluar los palindromos primos superiores
      if EsPalindromo (i) then
         if EsPrimo (i) then
            Put_Line
              ("Palindromo primo inmediatamente superior al entero positivo introducido:" &Integer'Image (i));
            exit;--Cuando printemos el primer palindromo primo, salimos del bucle, finalizamos la busqueda.
         end if;
      end if;
   end loop;
end Palindromo_TheEgg;
