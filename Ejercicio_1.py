using System;

namespace altura_de_personas
{
    class altura_de_personas
    {

        static void Main(string[] args)
        {
            int cantidad_de_personas = 0;
            float suma_de_alturas = 0;
            float promedio_de_alturas = 0;

            Console.Write("----- Cuantas personas quiere ingresar? ----- ");
            cantidad_de_personas = int.Parse(System.Console.ReadLine());

            float[] promedios = new float[cantidad_de_personas];
            for (int n = 0; n < promedios.Length; n++)
            {
                Console.Write($"Altura de las Personas en Centimetros {n+1} : ");
                promedios[n] = float.Parse(System.Console.ReadLine());
                suma_de_alturas += promedios[n];
                promedio_de_alturas = suma_de_alturas/cantidad_de_personas;
            }
            for (int n = 0; n < promedios.Length; n++){
            }
            Console.WriteLine("----------------------------------------"); 
            Console.WriteLine("Personas : "+ promedios.Length);   
            Console.WriteLine($"La altura Promedio es de:  {promedio_de_alturas}"); 

        }
    }
}