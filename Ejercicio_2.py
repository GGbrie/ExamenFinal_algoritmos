using System;

namespace ISR_de_empleados
{
    class ISR_de_empleados

    {
        static void Main(string[] args)
        {
            int i;
            double ISR, sueldo_a, sueldo_b, total_descuento;
            string nombre;
            for (i=1; i<=2; i++)
            {
                Console.WriteLine("---- Ingrese Datos: ----  " + i);
                Console.Write("Ingresa el nombre del empleado: ");
                nombre = Console.ReadLine();
                Console.Write("Su sueldo es de: ");
                sueldo_a = int.Parse(Console.ReadLine());
                if(sueldo_a>=300000)
                {
                    ISR=sueldo_a*0.5;
                }
                else
                {
                    ISR=sueldo_a*0.07;
                }
                total_descuento=ISR;
                sueldo_b=sueldo_a-total_descuento;
                Console.WriteLine("El Empleado debe de dar: " + nombre);
                Console.WriteLine("Valor de ISR: " + ISR);
                Console.WriteLine("Valor de total que debe de pagar es de: " + total_descuento);
                Console.WriteLine();
            }
        }
    }
}